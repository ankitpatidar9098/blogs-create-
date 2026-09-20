from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return HttpResponse("Welcome to Ankit's Django Project!")


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)