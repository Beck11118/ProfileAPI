from django.urls import path
from .views import UserCreateView, ProfileItemListCreateView, ProfileItemDetailView, ProfileItemFavoriteView

app_name = 'api'
urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('profileitems/', ProfileItemListCreateView.as_view(), name='profileitem-list'),
    path('profileitems/<int:pk>/', ProfileItemDetailView.as_view(), name='profileitem-detail'),
    path('profileitems/<int:pk>/favorite/', ProfileItemFavoriteView.as_view(), name='profileitem-favorite'),
]
