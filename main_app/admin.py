from django.contrib import admin
from .models import State, Territory, Place

# Register your models here.

admin.site.register(State)
admin.site.register(Territory)
admin.site.register(Place)