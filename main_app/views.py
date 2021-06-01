from django.shortcuts import render
from django.views import View  
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.


class Home(TemplateView):

    template_name = "home.html"


class Feed(TemplateView):
    template_name = "feed.html"


class UserProfile(TemplateView):
    template_name = "profile_detail.html"
