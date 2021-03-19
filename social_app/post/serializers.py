from rest_framework import serializers
from .models import Post


class PostSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'post',
            'user'
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
