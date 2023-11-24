from django.urls import path
from .views import UserCreateView, ProfileItemListCreateView, ProfileItemDetailView

app_name = 'api'
urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('profileitems/', ProfileItemListCreateView.as_view(), name='profileitem-list'),
    path('profileitems/<int:pk>/', ProfileItemDetailView.as_view(), name='profileitem-detail')
]
