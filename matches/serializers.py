from rest_framework import serializers
from .models import Match, Rating

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'user1', 'user2', 'match_date', 'status']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'match', 'rater', 'ratee', 'rating', 'comment', 'created_at']