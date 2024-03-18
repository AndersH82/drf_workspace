from django.urls import path
from .views import FriendshipList, FriendshipDetail

urlpatterns = [
    path('friendships/', FriendshipList.as_view(), name='friendship-list'),
    path(
        'friendships/<int:pk>/',
        FriendshipDetail.as_view(), name='friendship-detail'),
]
