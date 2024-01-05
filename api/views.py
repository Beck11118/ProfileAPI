from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from userprofile.models import ProfileItem, Education, Skill, Project, Testimonial, Service, Contact, Social, WorkExperience
from .serializers import ProfileItemSerializer, UserSerializer, EducationSerializer, SkillSerializer, ProjectSerializer, TestimonialSerializer, ServiceSerializer, ContactSerializer, SocialSerializer, WorkExperienceSerializer
from .filters import ProfileItemFilter, WorkExperienceFilter, EducationFilter
from .permissions import IsOwnerOrReadOnly

#PAGINATION AND FILTERING
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ProfileItemListCreateView(generics.ListCreateAPIView):
    queryset = ProfileItem.objects.all()
    serializer_class = ProfileItemSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
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
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    filterset_class = EducationFilter

class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


#WORK EXPERIENCE
class WorkExperienceListCreateView(generics.ListCreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    filterset_class = WorkExperienceFilter

class WorkExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


#SKILL
class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


#PROJECT
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


#TESTIMONIAL
class TestimonialListCreateView(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

class TestimonialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


#SERVICE
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


#SOCIAL
class SocialListCreateView(generics.ListCreateAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

class SocialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


#CONTACT
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]




  
