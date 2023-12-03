from django.urls import path
from .views import car_list, car_search, car_create, car_update, car_delete

urlpatterns = [
    path('cars/', car_list, name='car_list'),
    path('cars/search/', car_search, name='car_search'),
    path('cars/create/', car_create, name='car_create'),
    path('cars/update/<int:car_id>/', car_update, name='car_update'),
    path('cars/delete/<int:car_id>/', car_delete, name='car_delete'),
]