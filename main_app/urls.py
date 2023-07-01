from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('states/', views.StateList.as_view(), name="state_list"),
    path('territories/', views.TerritoryList.as_view(), name="territory_list"),
    path('places/', views.PlaceList.as_view(), name='place_list'),
]