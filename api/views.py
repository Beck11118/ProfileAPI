from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from userprofile.models import ProfileItem, Education
from .serializers import ProfileItemSerializer, UserSerializer, EducationSerializer
from .filters import ProfileItemFilter
from .permissions import IsOwnerOrReadOnly

#PAGINATION AND FILTERING
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ProfileItemListCreateView(generics.ListCreateAPIView):
    queryset = ProfileItem.objects.all()
    serializer_class = ProfileItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['name', 'skills']
    # search_fields = ['name', 'bio', 'skills', 'contact_info', 'education', 'experience']
    # ordering_fields = ['name', 'skills']
    # ordering = ['name']

    filterset_class = ProfileItemFilter

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class ProfileItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileItem.objects.all()
    serializer_class = ProfileItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileItemFavoriteView(generics.UpdateAPIView):
    queryset = ProfileItem.objects.all()
    serializer_class = ProfileItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.is_favorite = not profile.is_favorite()
        profile.save()
        serializer = self.get_serializer(profile)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

#EDUCATION
class EducationListCreateView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
        return super().perform_create(serializer)

class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsOwnerOrReadOnly]




  
