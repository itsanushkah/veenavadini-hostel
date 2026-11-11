"""URL routes for the Veena Vadini Girls Hostel site."""
from django.contrib import admin
from django.shortcuts import redirect
from django.templatetags.static import static
from django.urls import path

from wscubetech import views

urlpatterns = [
    path("", views.homePage),
    path("about-us/", views.aboutUS),
    path("service/", views.service, name="service"),
    path("gallery/", views.Gallery),
    path("contact-us/", views.contactus),
    path("admin/", admin.site.urls),
    # Browsers request /favicon.ico directly
    path("favicon.ico", lambda request: redirect(static("icons/favicon.ico"), permanent=True)),
]
