from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ProfilePictureViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'profile_pictures', ProfilePictureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
