from rest_framework import serializers
from .models import Friendship, User


class FriendshipSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Friendship
        fields = ['users', 'created_at']
