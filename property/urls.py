from django.urls import path
from .views import PropertyCreateView, PropertyListView

urlpatterns = [
    path('add/', PropertyCreateView.as_view(), name='property-add'),
    path('view/', PropertyListView.as_view(), name='property-view'),
]
