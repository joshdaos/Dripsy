from django.shortcuts import render, redirect
from django.views import View  
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import SellerProfile, Product
from django.views.generic.edit import UpdateView

from main_app import models


# Create your views here.


class Home(TemplateView):

    template_name = "home.html"


class UserProfile(TemplateView):
    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = SellerProfile.objects.get(user=self.request.user)
        return context


class UserProfileUpdate(UpdateView):
     model = SellerProfile
     fields = ['name','bio','image']
     template_name = "profile_update.html"
     success_url ="/profile/" 


class SellerList(TemplateView):
    template_name = "seller_list.html"


class ProductCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        sku = request.POST.get("sku")
        description = request.POST.get("description")
        image = request.POST.get("image")
        size = request.POST.get("size")
        seller = SellerProfile.objects.get(pk=pk)
        Product.objects.create(name=name, sku=sku, description=description, image=image, size=size, seller=seller)
        return redirect('profile_detail')


class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"
