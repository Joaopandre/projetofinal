from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('clube/', include('clube.urls')),
    path('admin/', admin.site.urls),
]