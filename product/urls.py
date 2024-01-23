from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('phone.html/',views.phone,name="phone"),
    path('computer.html/',views.computer,name="computer"),
    path('item/',views.item,name="item"),


]