
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage),
    path('signup/',views.signup),
    path('signview/',views.signview),
    path('login/',views.loginkaro),
    path('logindone/',views.logindone),
    path('logout/',views.logoutkaro),
    path('contact/',views.contactus),
    path('contactsubmit/',views.Contactsubmit),
]
