from django.urls import path, re_path
from .views import (
    CarCreateAPIView,
    CarListAPIView,
    CarRetrieveAPIView,
    CarDestroyAPIView,
    CarUpdateAPIView,
    CarListCreateAPIView,
    CarRetrieveUpdateAPIView,
    CarRetrieveDestroyAPIView,
    # car_search,
    PurchaseList
)

urlpatterns = [
    path('cars/', CarListAPIView.as_view(), name='car-list'),
    # path('cars/search/', car_search, name='car_search'),
    re_path('^cars/(?P<make>.+)/$', PurchaseList.as_view()),
    path('cars/create/', CarCreateAPIView.as_view(), name='car-create'),
    path('cars/<int:pk>/', CarRetrieveAPIView.as_view(), name='car-retrieve'),
    path('cars/<int:pk>/delete/', CarDestroyAPIView.as_view(), name='car-delete'),
    path('cars/<int:pk>/update/', CarUpdateAPIView.as_view(), name='car-update'),
    path('cars/list-create/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/retrieve-update/', CarRetrieveUpdateAPIView.as_view(), name='car-retrieve-update'),
    path('cars/<int:pk>/retrieve-destroy/', CarRetrieveDestroyAPIView.as_view(), name='car-retrieve-destroy'),
]