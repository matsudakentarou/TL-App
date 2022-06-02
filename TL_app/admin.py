from django.contrib import admin
from .models import (TLE, TL, TL_year)

admin.site.register(TLE)
admin.site.register(TL)
admin.site.register(TL_year)