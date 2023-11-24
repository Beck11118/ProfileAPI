from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from userprofile.models import ProfileItem
from .serializers import ProfileItemSerializer, UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ProfileItemListCreateView(generics.ListCreateAPIView):
    queryset = ProfileItem.objects.all()
    serializer_class = ProfileItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class ProfileItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileItem.objects.all()
    serializer_class = ProfileItemSerializer
    permission_classes = [permissions.IsAuthenticated]



  
