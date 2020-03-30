from django.urls import path     
from . import views

urlpatterns = [
    path('main', views.index),
    path('addUser', views.addUser),
    path('logUser', views.logUser),
    path('travel', views.travel),
    path('travel/create', views.createTrip),
    path('travel/add', views.addTrip),
    path('travel/destination/<int:id>', views.travelInfo),
    path('join/<int:id>', views.join),
    path('logout', views.logout),
]