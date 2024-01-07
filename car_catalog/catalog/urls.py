from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView


urlpatterns = [
    path('car/', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('', views.car_catalog, name='car_catalog'),
    path('car/add/', views.add_car, name='add_car'),
    path('car/<int:car_id>/edit/', views.edit_car, name='edit_car'),
    path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),
    path('car/purchase/<int:car_id>/', views.purchase_car, name='purchase_car'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('shop', views.send_email, name='send_email'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)