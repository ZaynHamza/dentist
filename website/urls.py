from django.urls import path
from . import views


urlpatterns = [
    path('appointment', views.appointment, name='appointment'),
    path('service', views.service, name='service'),
    path('pricing', views.pricing, name='pricing'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('', views.home, name='home'),
]