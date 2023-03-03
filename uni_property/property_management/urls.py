from django.urls import path
from . import views

app_name='property_management'

urlpatterns = [
    path('', views.index, name='index'), 
    path('Base-Template', views.base_template, name='base template'), 
    path('Properties-Management',views.properties_management, name='Properties Management'),
    path('Home-Improments', views.home_improments, name='Home Improments'),
    path('Mission', views.mission, name='mission'),
    path('Listing', views.rental, name='listing'),
    path('<int:listing_id>', views.single_rental, name='rental detail'),
]
