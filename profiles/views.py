from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializers


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers