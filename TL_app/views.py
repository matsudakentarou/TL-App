from multiprocessing import parent_process
from django.views.generic import View
from django.shortcuts import render
from .models import (TLE, TL, TL_year)
from django.http import JsonResponse
from django.db.models import Max, Min



class IndexView(View):

    def get(self, request, *args, **kwargs):
        parent_id = 1
        tl_data= TL.objects.filter(id=parent_id)
<<<<<<< HEAD
=======
        tl_year = TL_year.objects.order_by('tl_year').filter(id=parent_id)
>>>>>>> dd8416c3aebdffd5ab6cf222807d61fbb924d9ac
        tle_data = TLE.objects.order_by('start_at').filter(parent=parent_id)
        latest = TLE.objects.filter(parent=parent_id).aggregate(Max('end_at'))
        oldest= TLE.objects.filter(parent=parent_id).aggregate(Min('start_at'))
        for_range = [i for i in range(1800,2022)]
        context = {
            'for_range': for_range,
        }

        return render(request, 'app/index.html', {
            'tle_data': tle_data,
            'tl_data': tl_data,
            'tl_year': tl_year,
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


class SearchView(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        tle_data = TLE.objects.all()
        title_list = []

        if title:
            tle_data = tle_data.filter(title__icontains=title)

        for tle in tle_data:
            title_list.append(tle.title)

        data = {
            'title_list': title_list,
        }
        return JsonResponse(data)