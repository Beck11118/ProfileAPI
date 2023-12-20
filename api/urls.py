from django.urls import path
from .views import UserCreateView, ProfileItemListCreateView, ProfileItemDetailView, ProfileItemFavoriteView, EducationListCreateView, EducationDetailView, SkillListCreateView, SkillDetailView, ProjectListCreateView, ProjectDetailView, TestimonialListCreateView, TestimonialDetailView

app_name = 'api'
urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),

    #Profile Item
    path('profileitems/', ProfileItemListCreateView.as_view(), name='profileitem-list'),
    path('profileitems/<int:pk>/', ProfileItemDetailView.as_view(), name='profileitem-detail'),
    path('profileitems/<int:pk>/favorite/', ProfileItemFavoriteView.as_view(), name='profileitem-favorite'),

    #Education
    path('educations/', EducationListCreateView.as_view(), name='education-list'),
    path('educations/<int:pk>/', EducationDetailView.as_view(), name='education-detail'),

    #Skill
    path('skills/', SkillListCreateView.as_view(), name='skill-list'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),

    #Project
    path('projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    #Testimonial
    path('testimonials/', TestimonialListCreateView.as_view(), name='testimonial-list'),
    path('testimonials/<int:pk>/', TestimonialDetailView.as_view(), name='testimonial-detail'),
]
