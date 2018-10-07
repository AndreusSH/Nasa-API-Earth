
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
import pictures.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pictures.views.home, name = "home"),
    path('search', pictures.views.search, name = "search")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
