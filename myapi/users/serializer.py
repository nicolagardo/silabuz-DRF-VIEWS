from rest_framework import serializers
from .models import Users
from django.urls import path

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ('created_at',)