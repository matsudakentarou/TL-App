from django.views.generic import View
from django.shortcuts import render
from .models import (TLE, TL)
from django.http import JsonResponse


class IndexView(View):
    def get(self, request, *args, **kwargs):
        tle_data = TLE.objects.all()
        tl_title = TL.objects.filter(id=1)
        return render(request, 'app/index.html', {
            'tle_data': tle_data,
            'tl_title': tl_title,
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