from django.shortcuts import render, redirect
from django.views import View  
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import SellerProfile, Product, SellersFollowed
from django.views.generic.edit import UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from main_app import models


# Create your views here.


class Home(TemplateView):

    template_name = "home.html"
    
class Home(View):
   
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "home.html", context)


class Signup(View):

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        
        form = UserCreationForm(request.POST)

        name = request.POST.get("name")
        bio = request.POST.get("bio")
        image = request.POST.get("image")
    
        if form.is_valid():
            
            user = form.save()
            SellerProfile.objects.create(name=name, bio=bio, image=image, user=user)
            login(request, user)
            return redirect("profile_detail")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


@method_decorator(login_required, name='dispatch')
class About(TemplateView):

    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class SellerList(TemplateView):
    template_name = "seller_list.html"
    # add context here
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = SellerProfile.objects.get(user=self.request.user)
        return context


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


class ProductDelete(DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = "/profile/"


class ProductUpdate(UpdateView):
    model = Product 
    fields = ['name', 'sku', 'description', 'image', 'size']
    template_name = "product_update.html"
    success_url =  "/profile/"


class SellerDetail(DetailView):
    model = Product
    template_name = "seller_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = SellerProfile.objects.get(user=self.request.user)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["profile"] = SellersFollowed.objects.get(user=self.request.user)
    #     return context


class ErrorPage(TemplateView):
    
    template_name = "error_page.html"

