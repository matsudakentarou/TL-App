from multiprocessing import parent_process
from django.views.generic import View
from .models import (TLE, TL)
from django.http import JsonResponse
from django.db.models import Max, Min
from django.shortcuts import redirect, render
import json
from django.forms import model_to_dict
from .forms import TleForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        parent_id = 3
        form = TleForm()
        tl_data= TL.objects.filter(id=parent_id)
        tle_data = TLE.objects.order_by('start_at').filter(parent=parent_id)
        for_range = [i for i in range(1800,2022)]

        if request.headers.get("Content-Type") == "application/json":
            # すべてのtleを辞書型で受け取る
            tles = TLE.objects.values()
            tles_list = list(tles)
            # json形式でレスポンスを返す
            return JsonResponse(tles_list, safe=False, status=200)

        return render(request, 'app/index.html', {
            'tle_data': tle_data,
            'tl_data': tl_data,
            'for_range': for_range,
            'form':form,
        })