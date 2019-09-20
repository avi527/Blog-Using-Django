from django.contrib import admin
from django.urls import path,include
from techapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('techapp.urls')),
]
