from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index page'), 
    path('Properties_Management',views.Properties_Management, name='Properties Management page'),
    path('listing', views.listing, name='listing page'),
    path('Home_Improments', views.Home_Improments, name='Home Improments page'),
    path('Blogs', views.Blogs, name='Blogs page'),
]
