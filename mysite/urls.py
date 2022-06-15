from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TL_app.urls')),
] + static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)