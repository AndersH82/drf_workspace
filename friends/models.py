from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
