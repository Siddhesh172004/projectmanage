
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage),
    path('createproject/',views.createproject),
    path('uploadproject/',views.uploadproject),
    path('delete/<int:id>',views.Delete),
    path('edit/<int:id>',views.Edit),
    path('search/',views.Search),
    path('remarks/<int:id>',views.RemarksForm),
]
