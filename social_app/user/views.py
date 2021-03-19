from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserRegisterSerializer
from .models import User


# Create your views here.

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_user_profile(request, id):
    users = User.objects.filter(id=id)
    if users:
        serializer = UserSerializer(users, many=True)
        return Response({
            'data': serializer.data
        }, status=200)

    else:
        return Response({
            'message': 'Incorrect user id '
        }, status=404)


class UserView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        gender = request.POST.get('gender', None)

        if not all((name, email, password, gender)):
            return Response({
                'message': 'All fields are required: (name, email, password, gender)'
            }, status=404)

        user = User.objects.filter(email=email)
        if user:
            return Response({
                'message': 'Email already exist'
            }, status=404)

        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Registered successfully'
            }, status=201)

        else:
            return Response({
                'message': 'Error'
            }, status=404)

    def get(self, request, *args, **kwargs):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        if not all((email, password)):
            return Response({
                'message': 'All fields are required: (email, password)'
            }, status=404)

        users = User.objects.filter(email=email, password=password)
        if users:
            serializer = UserSerializer(users, many=True)
            return Response({
                'data': serializer.data
            }, status=200)

        else:
            return Response({
                'message': 'Incorrect account details'
            }, status=404)
