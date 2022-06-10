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
        parent_id = 1
        tl_data= TL.objects.filter(id=parent_id)
        tle_data = TLE.objects.order_by('start_at').filter(parent=parent_id)
        latest = TLE.objects.filter(parent=parent_id).aggregate(Max('end_at'))
        oldest= TLE.objects.filter(parent=parent_id).aggregate(Min('start_at'))
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
            'latest': latest['end_at__max'].year,
            'oldest': oldest['start_at__min'].year,
            'for_range': for_range,
        })
    
    def post(self, request):
        # json文字列を辞書型にし、pythonで扱えるようにする。
        tle = json.loads(request.body)
        form = TleForm(tle)

        # データが正しければ保存する。
        if form.is_valid():
            new_tle = form.save()
            return JsonResponse({"tle": model_to_dict(new_tle)}, status=200)
        return redirect("tle_list_url")
    


class TleView(View):
    def get(self, request):
        # リクエストがjson形式のとき
        if request.headers.get("Content-Type") == "application/json":
            # すべてのtleを辞書型で受け取る
            tles = TLE.objects.values()
            tles_list = list(tles)
            # json形式でレスポンスを返す
            return JsonResponse(tles_list, safe=False, status=200)
        return render(request, "app/index.html")

    def post(self, request):
        # json文字列を辞書型にし、pythonで扱えるようにする。
        tle = json.loads(request.body)
        form = TleForm(tle)

        # データが正しければ保存する。
        if form.is_valid():
            new_tle = form.save()
            return JsonResponse({"tle": model_to_dict(new_tle)}, status=200)
        return redirect("tle_list_url")

    def put(self, request):
        response = json.loads(request.body)
        # dbの中から、同じidのtleを取得する。
        tle = TLE.objects.get(id=response.get("id"))
        # タスクが完了していたら、未完了に、
        # タスクが未完了なら、完了にする
        if tle.completed:
            tle.completed = False
        else:
            tle.completed = True
        # 更新した内容を保存する。
        tle.save()
        return JsonResponse(model_to_dict(tle))

    def delete(self, request):
        response = json.loads(request.body)
        tle = TLE.objects.get(id=response.get("id"))
        # タスクを削除する
        tle.delete()
        return JsonResponse({"result": "Ok"})