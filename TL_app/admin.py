from django.contrib import admin
from .models import (TLE, TL, year)

admin.site.register(TLE)
admin.site.register(TL)
admin.site.register(year)