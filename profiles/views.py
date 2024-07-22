from rest_framework import viewsets
from .models import Profile, ProfilePicture
from .serializers import ProfileSerializer, ProfilePictureSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfilePictureViewSet(viewsets.ModelViewSet):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer
