from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import car_catalog


urlpatterns = [
    path('car/', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('car-catalog/', car_catalog, name='car_catalog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)