from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CollectAll.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('register.urls')),
]
