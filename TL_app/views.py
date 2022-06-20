from multiprocessing import parent_process
from django.urls import reverse_lazy
from django.views.generic import View
from .models import (TLE, TL)
from django.http import JsonResponse
from django.db.models import Max, Min
from django.shortcuts import redirect, render, resolve_url
import json
from django.forms import model_to_dict
from .forms import TleForm
from django.views.generic import CreateView

def index(request):
    parent_id = 1

    if request.method == "POST":
        form = TleForm()
        for_range = [i for i in range(1800,2022)]
        tl_data= TL.objects.filter(id=parent_id)
        tle_data = TLE.objects.order_by('-rank').filter(parent=parent_id)

        search_id = request.POST.get('radio_id',None)
        search_tle_data = TLE.objects.filter(id=search_id).first
        context ={
            'tle_data': tle_data,
            'tl_data': tl_data,
            'for_range': for_range,
            'search_id':search_id,
            'form':form,
            'search_tle_data':search_tle_data,
        }
    else:
        for_range = [i for i in range(1800,2022)]
        form = TleForm()
        tl_data= TL.objects.filter(id=parent_id)
        tle_data = TLE.objects.order_by('-rank').filter(parent=parent_id)

        search_id = 55
        search_tle_data = TLE.objects.filter(id=search_id).first
        context={
            'tle_data': tle_data,
            'tl_data': tl_data,
            'for_range': for_range,
            'form':form,
            'search_tle_data':search_tle_data,
        }

    return render(request, 'app/index.html', context)