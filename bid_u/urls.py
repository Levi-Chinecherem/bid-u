from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='main'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    path('causes/', views.causes_view, name='causes'),
    path('donation/', views.donate_view, name='donate'),
]