import json
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from .models import ServiceMonitorLog


def summary(request):
    """
    View for Summary

    This generate http response with a josin object for the summary of the
    monitoring status for last one hours.
    """
    data = dict()
    time_threshold = timezone.now() - timedelta(hours=1)
    logs = ServiceMonitorLog.objects.filter(log_time__gt=time_threshold)
    data['total_verified'] = logs.count()
    data['total_up'] = logs.filter(is_up=True).count()
    data['total_down'] = logs.filter(is_up=False).count()
    data['unique_sites'] = logs.values('site').distinct().count()
    data['unique_up_sites'] = logs.filter(is_up=True).values('site').distinct().count()
    data['unique_down_sites'] = logs.filter(is_up=False).values('site').distinct().count()
    return HttpResponse(json.dumps(data), content_type="application/json")