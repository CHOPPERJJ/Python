from django.urls import path, include
from django.contrib import admin
# from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
]
