from django.contrib import admin
from .models import Header, HeroSlider, AreasCovered, AboutUs, WhyChoosePropertyManagment, WhyChooseUs, Testimonials, ContactUs, Footer, GeneralInfo, OurMissionVision, OurPropertyManagement, OurPropertyManagementServices, FreePropertyManagement, PropertyHomeImprovements, OurServices, OurServicesdescription, Rental

# Register your models here.


class HeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'background_image']


class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ['order_no', 'image', 'is_active']


class AreasCoveredAdmin(admin.ModelAdmin):
    list_display = ['areas_name']


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description', 'button_name']


class WhyChoosePropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description']


class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_one', 'description']


class FooterAdmin(admin.ModelAdmin):
    list_display = ['description']


class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['mobile', 'email',
                    'insta_url', 'facbook_url', 'twitter_url']


class OurMissionVisionAdmin(admin.ModelAdmin):
    list_display = ['mission', 'vision']


class OurPropertyManagementAdmin(admin.ModelAdmin):
    list_display = ['services_one', 'services_two', 'services_three', 'services_four',
                    'services_five', 'services_six', 'services_seven', 'services_eight', 'image']


class OurPropertyManagementServicesAdmin(admin.ModelAdmin):
    list_display = ['description_one', 'description_two']


class FreePropertyManagementAdmin(admin.ModelAdmin):
    list_display = ['property_management_assessment_One', 'property_management_assessment_Two', 'property_management_assessment_Three', 'property_management_assessment_Four',
                    'property_management_assessment_Five', 'property_management_assessment_description_one', 'property_management_assessment_description_two']


class PropertyHomeImprovementsAdmin(admin.ModelAdmin):
    list_display = ['property_renovations_description']


class OurServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class OurServicesdescriptionAdmin(admin.ModelAdmin):
    list_display = ['our_services_main_description_one',
                    'our_services_main_description_two']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile',
                    'services', 'property_type', 'address', 'message', 'listing_id']


class RentalAdmin(admin.ModelAdmin):
    list_display = [
        "address", "bedroom", "bathroom", "street_address", "city", "province", "country", "postal_code", "listing_id", "ownership_type", "property_types", "is_pet_friendly", "price"
    ]



admin.site.register(Header, HeaderAdmin)
admin.site.register(HeroSlider, HeroSliderAdmin)
admin.site.register(AreasCovered, AreasCoveredAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(WhyChoosePropertyManagment, WhyChoosePropertyAdmin)
admin.site.register(WhyChooseUs, WhyChooseUsAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(GeneralInfo, GeneralInfoAdmin)
admin.site.register(OurMissionVision, OurMissionVisionAdmin)
admin.site.register(OurPropertyManagement, OurPropertyManagementAdmin)
admin.site.register(OurPropertyManagementServices, OurPropertyManagementServicesAdmin)
admin.site.register(FreePropertyManagement, FreePropertyManagementAdmin)
admin.site.register(PropertyHomeImprovements, PropertyHomeImprovementsAdmin)
admin.site.register(OurServices, OurServicesAdmin)
admin.site.register(OurServicesdescription, OurServicesdescriptionAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Rental, RentalAdmin)

