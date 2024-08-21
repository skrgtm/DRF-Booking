from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('property/', include('property.urls')),
    path('booking/', include('booking.urls')),
]
