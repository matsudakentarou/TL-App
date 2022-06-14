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


class IndexView(CreateView):
    model = TLE
    form_class = TleForm
    success_url = reverse_lazy('index')
    
    def get(self, request, *args, **kwargs):
        parent_id = 1
        form = TleForm()
        tl_data= TL.objects.filter(id=parent_id)
        tle_data = TLE.objects.order_by('start_at').filter(parent=parent_id)
        for_range = [i for i in range(1800,2022)]

        return render(request, 'app/index.html', {
            'tle_data': tle_data,
            'tl_data': tl_data,
            'for_range': for_range,
            'form':form,
        })

    def get_success_url(self):
        return resolve_url('index')

