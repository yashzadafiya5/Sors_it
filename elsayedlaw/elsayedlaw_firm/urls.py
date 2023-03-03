from django.urls import path
from . import views

app_name='elsayedlaw_firm'
urlpatterns = [
    path('', views.index, name='index'), 
    path('About-Us', views.about_us, name='about us'), 
    path('Immigration', views.immigration, name='immigration'), 
    path('Real-Estate', views.real_estate, name='real estate'), 
    path('Practice-Areas', views.practice_areas, name='practice areas'), 
    path('FAQ', views.faq, name='faq'), 
    path('Contact-Us', views.contact_us, name='contact us'), 
]
