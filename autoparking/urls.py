
from django.urls import path
from . import views

urlpatterns = [
    path('',views.trail),
    path('search',views.search),
]
