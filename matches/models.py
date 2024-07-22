from django.db import models
from users.models import User

class Match(models.Model):
    user1 = models.ForeignKey(User, related_name='match_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='match_user2', on_delete=models.CASCADE)
    match_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

class Rating(models.Model):
    match = models.ForeignKey(Match, related_name='ratings', on_delete=models.CASCADE)
    rater = models.ForeignKey(User, related_name='given_ratings', on_delete=models.CASCADE)
    ratee = models.ForeignKey(User, related_name='received_ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(6)])  # 0 to 5 stars
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)