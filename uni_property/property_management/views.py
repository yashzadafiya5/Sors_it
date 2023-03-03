from django.shortcuts import render, redirect,get_object_or_404
from .models import Header, HeroSlider, AreasCovered, AboutUs, WhyChoosePropertyManagment, WhyChooseUs, Testimonials, ContactUs, Footer, GeneralInfo, OurMissionVision, OurPropertyManagement, OurPropertyManagementServices, FreePropertyManagement, PropertyHomeImprovements, OurServices, OurServicesdescription, Rental
from django.db.models import Q
from django.db.models import Max
from blog.models import Blog
from django.contrib import messages
from django.utils import timezone


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        services = request.POST['service']
        address = request.POST['address']
        message = request.POST.get('message', 'No Message!')
        listing_id= request.POST.get('listing_id')
        if services == 'Property Management':
            property_type = request.POST['property_type']
            ContactUs.objects.create(name=name, email=email, mobile=mobile, services=services,
                                     address=address, message=message, property_type=property_type, listing_id=listing_id)
        elif services != 'Property Management':
            ContactUs.objects.create(
                name=name, email=email, mobile=mobile, services=services, address=address, message=message, listing_id=listing_id)
            
        return redirect('property_management:index')
    
    blog_details=Blog.objects.order_by('-publish_date')[:3]
    header = Header.objects.all().first()
    areas_coverd = AreasCovered.objects.all().first()
    about_us = AboutUs.objects.all().first()
    why_choose_property_management = WhyChoosePropertyManagment.objects.all()
    why_choose_us = WhyChooseUs.objects.all()
    testomonials = Testimonials.objects.filter(is_active=True)
    genral_info = GeneralInfo.objects.all().first()
    footer = Footer.objects.all().first()
    hero_slider = HeroSlider.objects.filter(is_active=True)[:6]
    data = {

        'hero_slider': hero_slider,
        'genral_info': genral_info,
        'footer': footer,
        'header': header,
        'about_us': about_us,
        'areas_coverd': areas_coverd,
        'why_choose_property_management': why_choose_property_management,
        'why_choose_us': why_choose_us,
        'testomonials': testomonials,
        'blog_details': blog_details
    }

    return render(request, 'index.html', data)


def base_template(request):
    hero_slider = HeroSlider.objects.filter(is_active=True)
    return render(request, 'base_template.html', {'hero_slider': hero_slider})


def mission(request):

    genral_info = GeneralInfo.objects.all().first()
    footer = Footer.objects.all().first()
    mission_vision = OurMissionVision.objects.all()
    properties_management = OurPropertyManagement.objects.all()

    data = {

        'mission_vision': mission_vision,
        'properties_management': properties_management,
        'genral_info': genral_info,
        'footer': footer

    }

    return render(request, 'mission.html', data)


def properties_management(request):

    genral_info = GeneralInfo.objects.all().first()
    footer = Footer.objects.all().first()
    properties_management_services = OurPropertyManagementServices.objects.all()
    property_management_assessment = FreePropertyManagement.objects.all()

    data = {

        'properties_management_services': properties_management_services,
        'property_management_assessment': property_management_assessment,
        'footer': footer,
        'genral_info': genral_info,
    }

    return render(request, 'properties-management.html', data)


def rental(request):
    filters={}
    bedroom=request.GET.get('bedroom')
    if bedroom != None and bedroom != 'Any':
        try:
            if bedroom[1] == '+':
                filters['bedroom__range']=(int(bedroom[0]), 999)
        except:
            filters['bedroom']=bedroom
        
    bathroom=request.GET.get('bathroom','Any')
    if bathroom != None and bathroom != 'Any':
        try:
            if bathroom[1] == '+':
                filters['bathroom__range']=(int(bathroom[0]), 999) 
        except:
            filters['bathroom']=bathroom    

    property_type=request.GET.get('property_type','Any')
    if property_type != None and property_type != 'Any':
        filters['property_types']=property_type   
        
    is_pet_friendly=request.GET.get('is_pet_friendly','Any')
    if is_pet_friendly != None and is_pet_friendly != 'Any':
        filters['is_pet_friendly']=is_pet_friendly

    genral_info = GeneralInfo.objects.first()
    footer = Footer.objects.first()
    rental_details = Rental.objects.filter(**filters)
    price=request.GET.get('sort_by')
    

    if price == 'maximum':
        rental_details=rental_details.order_by('-price')
    elif price == 'minimum':
        rental_details=rental_details.order_by('price')
        
    data = {
        'genral_info': genral_info,
        'footer': footer,
        'rental_details': rental_details,
    }

    return render(request, 'listing.html', data)


def single_rental(request, listing_id):
    single_rental_details = Rental.objects.get(listing_id=listing_id)
    genral_info = GeneralInfo.objects.all().first()
    footer = Footer.objects.all().first()

    data = {
        'genral_info': genral_info,
        'footer': footer,
        'single_rental_details': single_rental_details,
    }

    return render(request, 'single-listing.html', data)


def home_improments(request):

    genral_info = GeneralInfo.objects.all().first()
    footer = Footer.objects.all().first()
    property_home_improvements = PropertyHomeImprovements.objects.all()
    our_services = OurServices.objects.all()
    our_services_description = OurServicesdescription.objects.all()

    data = {

        'property_home_improvements': property_home_improvements,
        'our_services': our_services,
        'OurServicesDiscription': our_services_description,
        'footer': footer,
        'genral_info': genral_info,
    }

    return render(request, 'home-improments.html', data)

