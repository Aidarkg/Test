from django.contrib import admin
from django.urls import path, include
from flat.yasg import urlpatterns as yasg



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manager.urls')),
    path('', include('apartament.urls')),
]

urlpatterns += yasg