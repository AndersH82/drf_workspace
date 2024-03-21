from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    user1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friendships_as_user1')
    user2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friendships_as_user2')
    created_at = models.DateTimeField(auto_now_add=True)