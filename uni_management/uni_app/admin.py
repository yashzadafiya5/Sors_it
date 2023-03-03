from django.contrib import admin
from .models import *

# Register your models here.
class HeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'background_image']

class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ['image', 'order_no', 'is_active']

class AreasCoveredAdmin(admin.ModelAdmin):
    list_display = ['area_name_one', 'area_name_two', 'area_name_three',
                   'area_name_four', 'area_name_five', 'area_name_six', 'area_name_seven']

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'discriptiom', 'button_name']

class WhyChoosePropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'discriptiom']

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['image_one', 'name', 'image_two', 'image_three', 'description']

class FooterAdmin(admin.ModelAdmin):
    list_display = ['image', 'discription']

class GenralInfoAdmin(admin.ModelAdmin):
    list_display = ['mobile', 'email', 'insta_url', 'facbook_url', 'twitter_url']

class OurMissionVisionAdmin(admin.ModelAdmin):
    list_display = ['mission', 'vision', 'discription']

class OurPropertyManagementAdmin(admin.ModelAdmin):
    list_display = ['services_one', 'services_two', 'services_three', 'services_four', 'services_five', 'services_six', 'services_seven', 'services_eight', 'image']

class OurPropertyManagementServicesAdmin(admin.ModelAdmin):
    list_display = ['discription_one', 'discription_two']

class FreePropertyManagementAdmin(admin.ModelAdmin):
    list_display = ['property_management_assessment_One', 'property_management_assessment_Two', 'property_management_assessment_Three', 'property_management_assessment_Four', 'property_management_assessment_Five', 'property_management_assessment_description_one', 'property_management_assessment_description_two']

class PropertyHomeImprovementsAdmin(admin.ModelAdmin):
    list_display = ['property_renovations_description']

class OurServicesAdmin(admin.ModelAdmin):
    list_display = ['title','discription','our_services_main_description_one','our_services_main_description_two']

admin.site.register(Header,HeaderAdmin)
admin.site.register(HeroSlider,HeroSliderAdmin)
admin.site.register(AreasCovered,AreasCoveredAdmin)
admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(WhyChooseProperty,WhyChoosePropertyAdmin)
admin.site.register(WhyChooseUs,WhyChooseUsAdmin)
admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(Footer,FooterAdmin)
admin.site.register(GenralInfo,GenralInfoAdmin)
admin.site.register(OurMissionVision,OurMissionVisionAdmin)
admin.site.register(OurPropertyManagement,OurPropertyManagementAdmin)
admin.site.register(OurPropertyManagementServices,OurPropertyManagementServicesAdmin)
admin.site.register(FreePropertyManagement,FreePropertyManagementAdmin)
admin.site.register(PropertyHomeImprovements,PropertyHomeImprovementsAdmin)
admin.site.register(OurServices,OurServicesAdmin)
