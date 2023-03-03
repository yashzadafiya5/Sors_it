from django.db import models
from PIL import Image

# Create your models here.

class Header(models.Model):
    title = models.TextField(max_length=128)
    background_image = models.ImageField(upload_to='header_image')
    
    class Meta:
        verbose_name_plural = 'Headerssss'

# can have exactly six
class HeroSlider(models.Model):
    image = models.ImageField(upload_to='slider_image')
    order_no = models.IntegerField(default=50)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'HeroSlider'
        ordering = ['order_no']
        
class AreasCovered(models.Model):
    areas_name = models.TextField()
    class Meta:
        verbose_name_plural = 'AreasCovered'
        
class AboutUs(models.Model):
    title = models.TextField(max_length=128)
    image = models.ImageField(upload_to='about_us_image')
    description = models.TextField()
    button_name = models.CharField(max_length=20)
    
class WhyChoosePropertyManagment(models.Model):
    title = models.TextField(max_length=128)
    image = models.ImageField(upload_to='why_choose_property_image')

class WhyChooseUs(models.Model):
    title = models.TextField(max_length=128)
    image = models.ImageField(upload_to='why_choose_us_image')
    description = models.TextField()

class Testimonials(models.Model):
    image_one = models.ImageField(upload_to='testimonials_image')
    name=models.CharField(max_length=120)
    description=models.TextField()
    order_no = models.IntegerField(default=50)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Testimonial'
        ordering = ['order_no']
        
class ContactUs(models.Model):
    name=models.CharField(max_length=120)
    email = models.TextField()
    mobile = models.BigIntegerField()
    services = models.TextField()
    property_type = models.TextField(null=True, blank=True)
    address = models.TextField()
    message = models.TextField()
    listing_id = models.TextField(null=True, blank=True)

class Footer(models.Model):
    description = models.TextField()
    
class GeneralInfo(models.Model):
    mobile = models.BigIntegerField()
    email = models.TextField()
    insta_url = models.TextField()
    facbook_url = models.TextField()
    twitter_url = models.TextField()

class OurMissionVision(models.Model):
    mission = models.TextField()
    vision = models.TextField()

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
    description_one = models.TextField()
    description_two = models.TextField()
    
class FreePropertyManagement(models.Model):
    property_management_assessment_One=models.TextField(max_length=120)
    property_management_assessment_Two=models.TextField(max_length=120)
    property_management_assessment_Three=models.TextField(max_length=120)
    property_management_assessment_Four=models.TextField(max_length=120)
    property_management_assessment_Five=models.TextField(max_length=120)
    property_management_assessment_description_one=models.TextField()
    property_management_assessment_description_two=models.TextField()

class PropertyHomeImprovements(models.Model):
    property_renovations_description=models.TextField()
    
class OurServices(models.Model):
    title = models.TextField(max_length=60)
    description= models.TextField()
    
class OurServicesdescription(models.Model):
    our_services_main_description_one=models.TextField()
    our_services_main_description_two=models.TextField()

class Rental(models.Model):
    class PropertyType(models.TextChoices):
        appartment = "1", "Appartment"
        condo = "2", "Condo"
        du_fourplex = "3", "Du/Fourplex"
        house = "4", "House"
        hometown = "5", "Hometown"
        commercial = "6", "commercial"
        
    listing_id  = models.BigIntegerField(unique=True)
    rental_image_one=models.ImageField(upload_to='rental_images')
    rental_image_two=models.ImageField(upload_to='rental_images')
    rental_image_three=models.ImageField(upload_to='rental_images')
    rental_image_four=models.ImageField(upload_to='rental_images')
    rental_image_five=models.ImageField(upload_to='rental_images')
    price = models.IntegerField()
    address = models.TextField()
    bedroom = models.SmallIntegerField()
    bathroom = models.SmallIntegerField()
    street_address = models.TextField()
    city = models.CharField(max_length=120)
    province = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)
    ownership_type = models.CharField(max_length=120)
    property_description = models.TextField()
    
    property_types = models.CharField(
        max_length=2,
        choices=PropertyType.choices,
        default=PropertyType.house
    )
    
    is_pet_friendly = models.BooleanField(default=True)
    
    def get_is_pet_friendly(self):
        if self.is_pet_friendly:
            return 'Yes'
        return 'No'
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.rental_image_one.path)
        width, height = img.size
        new_height = int(width * 9 / 16)
        img = img.resize((width, new_height), Image.ANTIALIAS)
        img.save(self.rental_image_one.path)
        
