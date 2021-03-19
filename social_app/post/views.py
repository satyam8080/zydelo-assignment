from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import DocumentForm
from .serializers import PostSubmitSerializer, PostSerializer
from .models import Post
from follow.models import Follow
from user.models import User
from user.serializers import UserSerializer


# Create your views here.

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def delete_post_by_id(request, id):
    post = Post.objects.filter(id=id).first()
    if post:
        post.delete()
        return Response({
            'data': 'Post deleted'
        }, status=200)
    else:
        return Response({
            'message': 'Invalid post id'
        }, status=404)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def update_post_by_id(request, id):
    post = Post.objects.filter(id=id).first()
    if post:
        status = request.POST.get('post', None)
        post_image = request.POST.get('post_image', None)
        check = 0

        if status:
            check = 1
            post.post = status
        if post_image:
            check = 1
            post.post_image = post_image

        if check:
            post.save()
            post_updated = Post.objects.filter(id=id)
            serializer = PostSerializer(post_updated, many=True)
            return Response({
                'message': 'Updated successfully',
                'data': serializer.data
            }, status=200)
        else:
            return Response({
                'message': 'Please provide atleast one argument: (post, post_image)'
            }, status=404)
    else:
        return Response({
            'message': 'No post found by given id'
        }, status=404)


class PostView(APIView):
    def post(self, request, *args, **kwargs):
        status = request.POST.get('post', None)
        myfile = request.FILES['post_image']
        user = request.POST.get('user', None)

        if not all((status, myfile, user)):
            return Response({
                'message': 'All fields are required: (status, post_image)'
            }, status=404)

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        serializer = PostSubmitSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            p = Post.objects.latest('id')
            temp = Post.objects.filter(id=p.pk).first()
            temp.post_image = myfile.name
            temp.save()

            return Response({
                'message': 'Posted successfully',
                'file_url': uploaded_file_url
            }, status=201)

        else:
            return Response({
                'message': 'Error occur while posting'
            }, status=404)

    def get(self, request, id, *args, **kwargs):
        post = Post.objects.filter(id=id)
        if post:
            serializer = PostSerializer(post, many=True)
            return Response({
                'data': serializer.data
            }, status=200)

        else:
            return Response({
                'message': 'No post found for given post id'
            }, status=404)


class PostSelfView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id', None)
        post = Post.objects.filter(user=user_id)
        if post:
            serializer = PostSerializer(post, many=True)
            return Response({
                'data': serializer.data
            }, status=200)

        else:
            return Response({
                'message': 'No post done by the user'
            }, status=404)


class PostFollowersView(APIView):
    def get(self, request, *args, **kwargs):
        usr_id = []
        user_id = request.GET.get('user_id', None)
        follow = Follow.objects.filter(follow_by=user_id)
        if follow:
            for i in follow:
                usr_id.append(i.follow_on)

            post_data = Post.objects.filter(user__in=usr_id)

            if post_data:
                serializer = PostSerializer(post_data, many=True)
                return Response({
                    'data': serializer.data
                }, status=200)

            else:
                return Response({
                    'message': 'No post done by the user'
                }, status=404)
        else:
            return Response({
                'message': 'User has not following any one yet'
            }, status=404)
