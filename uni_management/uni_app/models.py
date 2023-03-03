from django.db import models

# Create your models here.

class Header(models.Model):
    title = models.TextField(max_length=128)
    background_image = models.ImageField(upload_to='header_image')
    
    class Meta:
        verbose_name_plural = 'Headerssss'

class HeroSlider(models.Model):
    image = models.ImageField(upload_to='slider_image')
    order_no = models.IntegerField(default=50)
    is_active = models.BooleanField(default=True)
    
class AreasCovered(models.Model):
    area_name_one = models.TextField()
    area_name_two = models.TextField()
    area_name_three = models.TextField()
    area_name_four = models.TextField()
    area_name_five = models.TextField()
    area_name_six = models.TextField()
    area_name_seven = models.TextField()
   
class AboutUs(models.Model):
    title = models.TextField(max_length=128)
    image = models.ImageField(upload_to='about_us_image')
    discriptiom = models.TextField()
    button_name = models.CharField(max_length=20)

class WhyChooseProperty(models.Model):
    title = models.TextField(max_length=128)
    image = models.ImageField(upload_to='why_choose_property_image')

class WhyChooseUs(models.Model):
    title = models.TextField(max_length=128)
    image = models.ImageField(upload_to='why_choose_us_image')
    discriptiom = models.TextField()

class Testimonials(models.Model):
    image_one = models.ImageField(upload_to='testimonials_image')
    name=models.CharField(max_length=40)
    image_two = models.ImageField(upload_to='testimonials_image')
    image_three = models.ImageField(upload_to='testimonials_image')
    description=models.TextField()
    
class ContactUs(models.Model):
    name = models.TextField(max_length=40)
    email = models.TextField()
    mobile = models.CharField(max_length=20)
    services = models.TextField()
    property_type = models.TextField(null=True, blank=True)
    address = models.TextField()
    message = models.TextField()

class Footer(models.Model):
    image = models.ImageField(upload_to='footer_image')
    discription = models.TextField()
    
class GenralInfo(models.Model):
    mobile = models.CharField(max_length=20)
    email = models.TextField()
    insta_url = models.TextField()
    facbook_url = models.TextField()
    twitter_url = models.TextField()

class OurMissionVision(models.Model):
    mission = models.TextField(max_length=128)
    vision = models.TextField(max_length=128)
    discription = models.TextField()

class OurPropertyManagement(models.Model):
    services_one = models.TextField(max_length=60)
    services_two = models.TextField(max_length=60)
    services_three = models.TextField(max_length=60)
    services_four = models.TextField(max_length=60)
    services_five = models.TextField(max_length=60)
    services_six = models.TextField(max_length=60)
    services_seven = models.TextField(max_length=60)
    services_eight = models.TextField(max_length=60)
    image = models.ImageField(upload_to='property_image')

class OurPropertyManagementServices(models.Model):
    discription_one = models.TextField()
    discription_two = models.TextField()
    
class FreePropertyManagement(models.Model):
    property_management_assessment_One=models.TextField(max_length=120)
    property_management_assessment_Two=models.TextField(max_length=120)
    property_management_assessment_Three=models.TextField(max_length=120)
    property_management_assessment_Four=models.TextField(max_length=120)
    property_management_assessment_Five=models.TextField(max_length=120)
    property_management_assessment_description_one=models.TextField()
    property_management_assessment_description_two=models.TextField()

class PropertyContactUs(models.Model):
    name = models.TextField(max_length=40)
    email = models.TextField()
    mobile = models.CharField(max_length=20)
    services = models.TextField()
    property_type = models.TextField(null=True, blank=True)
    address = models.TextField()
    message = models.TextField()

class PropertyHomeImprovements(models.Model):
    property_renovations_description=models.TextField()
    
class OurServices(models.Model):
    title = models.TextField(max_length=60)
    discription= models.TextField()
    our_services_main_description_one=models.TextField()
    our_services_main_description_two=models.TextField()
    
class HomeImpromentsContactUs(models.Model):
    name = models.TextField(max_length=40)
    email = models.TextField()
    mobile = models.CharField(max_length=20)
    services = models.TextField()
    property_type = models.TextField(null=True, blank=True)
    address = models.TextField()
    message = models.TextField()