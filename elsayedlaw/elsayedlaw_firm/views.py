from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        name=request.POST.get('name') 
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        service=request.POST.get('service')
        message=request.POST.get('message')
        print(name,email,mobile,service,message)
        return redirect('elsayedlaw_firm:index')
    return render(request,'index.html')

def about_us(request):
    return render(request,'about-us/index.html')

def immigration(request):
    return render(request,'immigration/index.html')

def real_estate(request):
    return render(request,'real-estate/index.html')

def practice_areas(request):
    return render(request,'practice-areas/index.html')

def faq(request):
    return render(request,'faq/index.html')

def contact_us(request):
    return render(request,'contact-us/index.html')
