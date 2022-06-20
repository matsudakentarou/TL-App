from django.urls import path
from TL_app import views

urlpatterns = [
    path('', views.index, name='index'),
]