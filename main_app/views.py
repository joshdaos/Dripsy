from django.shortcuts import render
from django.views import View  
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import SellerProfile
from django.views.generic.edit import UpdateView


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


