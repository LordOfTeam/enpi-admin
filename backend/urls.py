from django.urls import path

from backend.api import views

urlpatterns = [
    path('api/place-lists', views.PlaceListView.as_view()),
    path('api/place-detail/<int:pk>', views.PlaceDetailView.as_view()),
]
