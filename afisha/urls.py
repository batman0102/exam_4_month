from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from film.views import main_view, films_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view),
    path("films/", films_view, name='films'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
