from django.urls import path
from . import views
from django.urls import path
from .views import protected_view

urlpatterns = [
    path('protected/', protected_view, name='protected_view'),
    path('', views.home, name = 'home')
]