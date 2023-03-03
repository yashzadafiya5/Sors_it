from django.shortcuts import render
from property_management.models import GeneralInfo,Footer
from .models import Blog
from django.utils import timezone

# Create your views here.
def blog_detail(request,slug):
    current_datetime = timezone.now()
    genral_info = GeneralInfo.objects.all().first()
    footer = Footer.objects.all().first()
    blog_details=Blog.objects.get(slug=slug)
    related_blogs = Blog.objects.filter(publish_date__lte=current_datetime.date()).exclude(slug=blog_details.slug).order_by('?')[:3]
    
    data={
        'blog': blog_details ,
        'related_blogs':related_blogs, 
        'genral_info':genral_info,
        'footer':footer
    }
    return render(request, 'blogs.html',data)

def blogs(request):
    current_datetime = timezone.now()
    blogs=Blog.objects.filter(publish_date__lte=current_datetime.date())
    genral_info = GeneralInfo.objects.all().first()
    footer = Footer.objects.all().first()

    data = {
        'blogs':blogs,
        'genral_info': genral_info,
        'footer': footer
        }
  
    return render(request, 'blogs-list.html', data)
