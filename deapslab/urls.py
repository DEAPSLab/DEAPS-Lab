from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('nitin-auluck/', views.nitin_auluck, name='nitin_auluck'),
    path('members/', views.members, name='members'),
    path('research/', views.research, name='research'),
    path('publications/', views.publications, name='publications'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('news-events/', views.news_events, name='news_events'),
    path('resources/', views.resources, name='resources'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('alumni/', views.alumni, name='alumni'),
]