
from django.contrib import admin
from django.urls import path
import pictures.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pictures.views.home, name = "home"),
    path('search', pictures.views.search, name = "search")
]
