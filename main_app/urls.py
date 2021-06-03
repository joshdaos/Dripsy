from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('feed/', views.SellerList.as_view(), name="feed"),
    path('profile/', views.UserProfile.as_view(), name="profile_detail"),
    path('profile/<int:pk>/', views.UserProfileUpdate.as_view(), name="profile_update"),
    path('profile/<int:pk>/products/new',
         views.ProductCreate.as_view(), name="product_create"),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name="product_detail"),
]