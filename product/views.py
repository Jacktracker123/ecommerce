from django.shortcuts import render
from . models import *
from . forms import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def phone(request):
    phn=Phone.objects.all()
    return render(request,'phone.html',{'phn':phn})

def computer(request):
    if request.method=="POST":
        a=Computer_form(request.POST)
        if a.is_valid():
            a.save()
    c=Computer_form()
    comp=Computer.objects.all()
    context={}
    context['c']=c
    context['comp']=comp
    return render(request,'computer.html',context)

def item(request):
    if request.method=="POST":
        a=Phone_form(request.POST)
        if a.is_valid():
            b=a.cleaned_data['name']
            c=a.cleaned_data['image']
            d=a.cleaned_data['price']
            data=Phone.objects.create(name=b,image=c,price=d)
            data.save()
    itm=Phone_form()
    return render(request,'item.html',{'itm':itm})

