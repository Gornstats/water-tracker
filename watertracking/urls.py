from django.urls import path

from .views import water_list, water_drunk

urlpatterns = [
    path('', water_list, name='water_list'),
    path('drunk/<int:pk>/<int:drunk>/', water_drunk, name='water_drunk'),
]
