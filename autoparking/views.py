from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import thinkvision


# Create your views here.
def trail(requests):
    return HttpResponse ('no merrcy'),

def search(requests):
    tv = thinkvision.objects.get(device_id='mypark')
    
    return JsonResponse({'slot_1_status':tv.slot1,'slot_2_status':tv.slot2})



    

