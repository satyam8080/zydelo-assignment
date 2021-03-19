from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FollowSerializer
from user.serializers import UserSerializer

from .models import Follow
from user.models import User


# Create your views here.

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def follow(request, user_id):
    follow_by = request.GET.get('user_id', None)

    # user = User.objects.filter(id=user_id)
    # if user:
    #     follow = Follow.objects.filter(follow_by=follow_by, follow_on=user_id)
    #     if follow:
    #         follow.delete()
    #         return Response({
    #             'data': 'User unfollowed'
    #         }, status=200)
    #     else:
    #         serializer = FollowSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({
    #                 'message': 'User followed '
    #             }, status=200)
    #         else:
    #             return Response({
    #                 'message': 'Error occur while following'
    #             }, status=404)
    # else:
    #     return Response({
    #         'message': 'User does not exist'
    #     }, status=404)


class FollowView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        follow_by = request.GET.get('user_id', None)

        user = User.objects.filter(id=user_id).first()
        user_main = User.objects.filter(id=follow_by).first()

        if user:
            follow = Follow.objects.filter(follow_by=follow_by, follow_on=user_id)
            if follow:
                follow.delete()

                user.followers = user.followers - 1
                user.save()
                user_main.followings = user_main.followings - 1
                user_main.save()

                return Response({
                    'data': 'User unfollowed'
                }, status=200)
            else:
                follow_obj = Follow(follow_by=follow_by, follow_on=user_id)
                follow_obj.save()

                user.followers = user.followers + 1
                user.save()
                user_main.followings = user_main.followings + 1
                user_main.save()

                return Response({
                    'message': 'User followed '
                }, status=200)
        else:
            return Response({
                'message': 'User does not exist'
            }, status=404)


class FollowingListView(APIView):
    def get(self, request, *args, **kwargs):
        usr_id = []
        user_id = request.GET.get('user_id', None)
        follow = Follow.objects.filter(follow_by=user_id)
        if follow:
            for i in follow:
                usr_id.append(i.follow_on)

            usr_data = User.objects.filter(id__in=usr_id)
            usr_serializer = UserSerializer(usr_data, many=True)
            return Response({
                'data': usr_serializer.data  # serializer.data
            }, status=200)
        else:
            return Response({
                'message': 'Not following any one'
            }, status=404)


class FollowListView(APIView):
    def get(self, request, *args, **kwargs):
        usr_id = []
        user_id = request.GET.get('user_id', None)
        follow = Follow.objects.filter(follow_on=user_id)
        if follow:
            for i in follow:
                usr_id.append(i.follow_by)

            usr_data = User.objects.filter(id__in=usr_id)
            usr_serializer = UserSerializer(usr_data, many=True)
            return Response({
                'data': usr_serializer.data  # serializer.data
            }, status=200)
        else:
            return Response({
                'message': 'Not followed by any one'
            }, status=404)
