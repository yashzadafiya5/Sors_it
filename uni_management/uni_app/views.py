from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    if request.method=="POST":
        return HttpResponse('message sent')
    header=Header.objects.all()
    hero_slider=HeroSlider.objects.all()
    areas_coverd=AreasCovered.objects.all()
    whychooseproperty=WhyChooseProperty.objects.all()
    whychooseus=WhyChooseUs.objects.all()
    return render(request,'index.html',{'header':header,'hero_slider':hero_slider,'areas_coverd':areas_coverd,'whychooseproperty':whychooseproperty,'whychooseus':whychooseus,})
        

def Properties_Management(request):
    return render(request,'properties-management.html')

def listing(request):
    return render(request,'listing.html')

def Home_Improments(request):
    return render(request,'home-improments.html')

def Blogs(request):
    return render(request,'blogs-list.html')

