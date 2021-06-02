from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('feed/', views.SellerList.as_view(), name="feed"),
    path('profile/', views.UserProfile.as_view(), name="profile_detail"),
]