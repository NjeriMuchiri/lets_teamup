from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home_page"),
    path('room/<str:pk>/', views.rooms, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
]
