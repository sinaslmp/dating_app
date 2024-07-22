from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, UserViewSet, GenderViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'genders', GenderViewSet)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('', include(router.urls)),
]
