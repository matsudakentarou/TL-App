from multiprocessing import parent_process
from django.views.generic import View
from django.shortcuts import render
from .models import (TLE, TL)
from django.http import JsonResponse
from django.db.models import Max, Min

class IndexView(View):
    def get(self, request, *args, **kwargs):
        parent_id = 1
        tl_data= TL.objects.filter(id=parent_id)
        tle_data = TLE.objects.order_by('start_at').filter(parent=parent_id)
        latest = TLE.objects.filter(parent=parent_id).aggregate(Max('end_at'))
        oldest= TLE.objects.filter(parent=parent_id).aggregate(Min('start_at'))
        for_range = [i for i in range(1800,2022)]

        return render(request, 'app/index.html', {
            'tle_data': tle_data,
            'tl_data': tl_data,
            'latest': latest['end_at__max'].year,
            'oldest': oldest['start_at__min'].year,
            'for_range': for_range,
        })


class AddView(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')

        tle = TLE()
        tle.title = title

        tle.save()

        data = {
            'title': title,

        }
        return JsonResponse(data)