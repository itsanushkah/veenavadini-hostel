"""
URL configuration for wscubetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings

from django.urls import path
from wscubetech import views
from django.conf.urls.static import static

urlpatterns = [
    #html page render
    path('',views.homePage),
    path('contact-us/',views.contactus),
    #static url
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutUS),
     path('course/',views.Course),
    # to uconnect page using django inbuilt 
     path('service/',views.service,name="service"),
    
    path('gallery/',views.Gallery),

    #dynamic url
    path('course/<courseid>',views.CourseDetails),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])