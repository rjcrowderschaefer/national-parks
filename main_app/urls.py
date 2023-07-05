from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('states/', views.StateList.as_view(), name="state_list"),
    path('states/<int:pk>/', views.StateDetail.as_view(), name = "state_detail"),
    path('territories/', views.TerritoryList.as_view(), name="territory_list"),
    path('territories/<int:pk>/', views.TerritoryDetail.as_view(), name = "territory_detail"),
    # path('places/', views.PlaceList.as_view(), name='place_list'),
    path('states/new/', views.PlaceCreate.as_view(), name="place_create"),
    path('territories/new/', views.PlaceTerritoryCreate.as_view(), name="place_territory_create")
]