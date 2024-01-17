from django.shortcuts import render
from . models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def phone(request):
    phn=Phone.objects.all()
    return render(request,'phone.html',{'phn':phn})

def computer(request):
    comp=Computer.objects.all()
    return render(request,'computer.html',{'comp':comp})