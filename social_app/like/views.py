from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from post.models import Post
from rest_framework.response import Response

from .models import Like


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def like_post(request, post_id):
    user_id = request.GET.get('user_id', None)
    post = Post.objects.filter(id=post_id).first()
    if post:
        like = Like.objects.filter(likeBy=user_id, likeOn=post_id)

        if like:
            like.delete()
            post.likes_count = post.likes_count - 1
            post.save()

            return Response({
                'data': 'Post Dis-liked'
            }, status=200)
        else:
            l = Like(likeBy=user_id, likeOn=post_id)
            l.save()
            post.likes_count = post.likes_count + 1
            post.save()

            return Response({
                'data': 'Post Liked'
            }, status=200)
    else:
        return Response({
            'data': 'Invalid post id'
        }, status=404)
