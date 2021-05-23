import imp
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import NavigationRecord

def home(request):
    # get NavigationRecord datas where datetime >= 2 days ago, which is last 48 hours
    # converting QuerySet to list for easy converting to JSON
    data_list = NavigationRecord.objects.filter(datetime__gte=timezone.now()-timedelta(days=2))
    parsed_data_list = []
    for data in data_list:
        parsed_data_list.append(
            {
                'latitude': data.latitude,
                'longitude':data.longitude,
                'vehicle_plate': data.vehicle.plate,
                'datetime': data.datetime.strftime('%d.%m.%Y %H:%M:%S'),
            }
        )
    # given indent for pretty print
    return JsonResponse(parsed_data_list, safe=False, json_dumps_params={'indent': 2})
