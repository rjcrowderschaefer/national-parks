from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import State, Territory

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

# class State:
#     def __init__(self, name, image, parknum):
#         self.name = name
#         self.image = image
#         self.parknum = parknum

# class Territory:
#     def __init__(self, name, image, parknum):
#         self.name = name
#         self.image = image
#         self.parknum = parknum

# class Park:
#     def __init__(self, name, image, parktype, location, description):
#         self.name = name
#         self.image = image
#         self.parktype = parktype
#         self.image = location
#         self.description = description

# states = [
#     State('Alaska', 'https://ivintageimages.com/cdn/shop/products/QBSTLL_002-webscan_40c57991-2448-4d8a-8c13-fef824796087_1024x1024@2x.jpg?v=1617294483', 23),
#     State('Arizona', 'https://ivintageimages.com/cdn/shop/products/QBSTLL_003-webscan_1024x1024@2x.jpg?v=1554321905', 22),
#     State('California', 'https://ivintageimages.com/cdn/shop/products/QBSTLL_005-webscan_1024x1024@2x.jpg?v=1554322013', 28),
#     State('Colorado', 'https://ivintageimages.com/cdn/shop/products/QBSTLL_006-webscan_1024x1024@2x.jpg?v=1554322100', 13),
# ]

# territories = [
#     Territory('American Samoa', 'https://i.etsystatic.com/27583120/r/il/ae2bdc/2840534200/il_794xN.2840534200_4nt9.jpg', 1),
#     Territory('Guam', 'https://www.squadronposters.com/wp-content/uploads/Apra_Harbor_Guam_Sub_16x20_SP00921Mfeatured-aircraft-lithograph-vintage-airplane-poster.jpg', 1),
# ]

class StateList(TemplateView):
    template_name = "states_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        return context
    
class TerritoryList(TemplateView):
    template_name = "territories_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["territories"] = Territory.objects.all()
        return context