from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import car_catalog


urlpatterns = [
    path('car/', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('', views.car_catalog, name='car_catalog'),
    path('car/add/', views.add_car, name='add_car'),
    path('car/<int:car_id>/edit/', views.edit_car, name='edit_car'),
    path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),
    path('car/purchase/<int:car_id>/', views.purchase_car, name='purchase_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)