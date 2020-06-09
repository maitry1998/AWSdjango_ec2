from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from djangofirst import views
urlpatterns = [
    path('', views.index, name="index"),
    path("help/", views.form_function),

]
