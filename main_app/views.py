from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(View):
    def get(self, request):
        return HttpResponse("About Page")
    
# class State:
#     def __init__(self, name, image, description):
#         self.name = name
#         self.image = image
#         self.description = description
