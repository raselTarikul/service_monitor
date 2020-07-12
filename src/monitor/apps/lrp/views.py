from django.shortcuts import render
from django.http import HttpResponse
from .models import ServiceMonitorLog

# Create your views here.


def home(request):
    count = ServiceMonitorLog.objects.all().count()
    return HttpResponse(count)