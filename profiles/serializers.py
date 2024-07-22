from rest_framework import serializers
from .models import Profile, ProfilePicture

class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ['id', 'image']

class ProfileSerializer(serializers.ModelSerializer):
    pictures = ProfilePictureSerializer(many=True, read_only=True)
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'interests', 'preferences', 'pictures']
