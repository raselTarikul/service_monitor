from django.urls import path
from .views import summary

urlpatterns = [
    path('', summary, name='summary'),

]