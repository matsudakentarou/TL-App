from django.urls import reverse
from multiprocessing import parent_process
from django.urls import reverse_lazy
from django.views.generic import View
from .models import (TLE, TL)
from django.http import JsonResponse
from django.db.models import Max, Min
from django.shortcuts import redirect, render
import json
from django.forms import model_to_dict
from .forms import TleForm
from django.views.generic import CreateView


def index(request):
    parent_id = 1

    if request.method == "POST":
        if 'radio_id' in request.POST:
            form = TleForm()
            for_range = [i for i in range(1800,2023)]
            tl_data= TL.objects.all().first
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
            object = TLE.objects.create(
                title = request.POST['title'],
                year  = request.POST['year'],
                rank = request.POST['rank'],
                image = request.POST['image'],
                video = request.POST['video'],
                map = request.POST['map'],
                body = request.POST['body']
                )
            object.save()
            return redirect('index')
    else:
        for_range = [i for i in range(1800,2022)]
        form = TleForm()
        tl_data= TL.objects.all().first
        tle_data = TLE.objects.order_by('-rank').filter(parent=parent_id)
        context={
            'tle_data': tle_data,
            'tl_data': tl_data,
            'for_range': for_range,
            'form':form,
        }

    return render(request, 'app/index.html', context)