from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('feed/', views.SellerList.as_view(), name="feed"),
    path('profile/', views.UserProfile.as_view(), name="profile_detail"),
    path('profile/<int:pk>/', views.UserProfileUpdate.as_view(), name="profile_update"),
    path('profile/<int:pk>/products/new',
         views.ProductCreate.as_view(), name="product_create"),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name="product_detail"),
    path('product/<int:pk>/delete', views.ProductDelete.as_view(), name="product_delete"),
    path('product/<int:pk>/update', views.ProductUpdate.as_view(), name="product_update"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('seller/<int:pk>/', views.SellerDetail.as_view(), name="seller_detail"),
    path('error/', views.ErrorPage.as_view(), name="error_page"),
]