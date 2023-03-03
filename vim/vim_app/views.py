from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ContactUs
# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mnumber']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        ContactUs.objects.create(name=name,mobile=mobile,email=email,subject=subject,message=message)
        return redirect("vim:index page")
    return render(request,'index.html')

def About_Us(request):
    return render(request,'About copy.html')

def Products(request):
    return render(request,'Products.html')
