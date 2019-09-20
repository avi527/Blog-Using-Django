from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('registration/', views.registration, name='registration'),
    path('updImage/', views.updImage, name='updImage'),
    path('ssession/', views.setsession,name='ssession'),
    path('gsession/', views.getsession,name='gsession'),
    path('scookie/', views.setcookie,name='scookie'),
    path('gcookie/', views.getcookie,name='gcookie'),
    path('addpost/', views.addpost,name='addpost'),
    path('showpost/', views.showpost,name='showpost')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)