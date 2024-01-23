from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('phone/',views.phone,name="phone"),
    path('computer/',views.computer,name="computer"),
    path('item/',views.item,name="item"),


]