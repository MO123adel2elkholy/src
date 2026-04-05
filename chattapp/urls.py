from django.urls import path, include
from django.contrib import admin
from . import views
# from .views import  base
# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:pk>', views.detail, name='detail'),
]
