from rest_framework import serializers

from .models import Project

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email")

class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ("user","id","title","description","link")

