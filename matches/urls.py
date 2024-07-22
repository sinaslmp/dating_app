from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'matches', MatchViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
