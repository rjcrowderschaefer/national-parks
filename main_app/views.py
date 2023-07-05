from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import State, Territory, Place, PlaceTerritory
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        context['territories'] = Territory.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        context["territories"] = Territory.objects.all()
        return context

class StateList(TemplateView):
    template_name = "states_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["territories"] = Territory.objects.all()
        name = self.request.GET.get("name")
        if name != None:
            context["states"] = State.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["states"] = State.objects.all()
            context["header"] = "States with National Parks"
        return context
    
class StateDetail(DetailView):
    model = State
    template_name = "state_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        context["territories"] = Territory.objects.all()
        return context
    
class StateUpdate(UpdateView):
    model = State
    fields = ['name', 'image', 'parknum']
    template_name = "state_update.html"
    
    def get_success_url(self):
        return reverse('state_detail', kwargs={'pk': self.object.pk})

class StateDelete(DeleteView):
    model = State
    template_name = "state_delete_confirmation.html"
    success_url = "/states/"

class TerritoryList(TemplateView):
    template_name = "territories_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        name = self.request.GET.get("name")
        if name != None:
            context["territories"] = Territory.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["territories"] = Territory.objects.all()
            context["header"] = "Territories with National Parks"
        return context

class TerritoryDetail(DetailView):
    model = Territory
    template_name = "territory_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        context["territories"] = Territory.objects.all()
        return context
    
class TerritoryUpdate(UpdateView):
    model = Territory
    fields = ['name', 'image', 'parknum']
    template_name = "territory_update.html"

    def get_success_url(self):
        return reverse('territory_detail', kwargs={'pk': self.object.pk})

class TerritoryDelete(DeleteView):
    model = Territory
    template_name = "territory_delete_confirmation.html"
    success_url = "/territories/"

# class PlaceList(TemplateView):
#     template_name = "places_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["places"] = Place.objects.all()
#         context["states"] = State.objects.all()
#         context["territories"] = Territory.objects.all()
#         return context
    
class PlaceCreate(CreateView):
    model = Place
    fields = ['name', 'image', 'placetype', 'description', 'state']
    template_name = "place_create.html"
    success_url = "/states/"
    # How do I reroute to the state detail page when adding a new place? I think I need to use the state's fk instead of pk.
    # def get_success_url(State):
    #     return reverse('state_detail', kwargs={'pk': State.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        context["territories"] = Territory.objects.all()
        return context

class PlaceTerritoryCreate(CreateView):
    model = PlaceTerritory
    fields = ['name', 'image', 'placetype', 'description', 'territory']
    template_name = "place_territory_create.html"
    success_url = "/territories/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        context["territories"] = Territory.objects.all()
        return context