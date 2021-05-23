import imp
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import NavigationRecord

def home(request):
    # get NavigationRecord datas where datetime >= 2 days ago, which is last 48 hours
    # converting QuerySet to list for easy converting to JSON
    data = list(NavigationRecord.objects.filter(datetime__gte=timezone.now()-timedelta(days=2)).values())
    # given indent for pretty print
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})
