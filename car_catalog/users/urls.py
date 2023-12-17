from django.urls import path
from . import views
from django.urls import path
from .views import protected_view


urlpatterns = [
    path('', views.home, name = 'home'),
    path('protected/', protected_view, name='protected_view'),
]