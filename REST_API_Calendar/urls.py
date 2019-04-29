from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/', include('main.urls', namespace="main")),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('holidays/', include('holidays.urls', namespace="holidays"))
]
