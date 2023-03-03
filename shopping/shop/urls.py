from django.urls import path 
from . import views 

app_name = 'vim'
urlpatterns = [
    path('',views.index,name='index page'),
    path('about-us',views.About_Us,name='about-us page'),
    path('products',views.Products,name='products page'),
]
