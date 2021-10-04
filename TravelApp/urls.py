from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('addUser', views.addUser),
    path('logUser', views.logUser),
    path('travel', views.travel),
    path('travel/create', views.createTrip),
    path('travel/delete/<int:id>', views.deleteTrip),
    path('travel/add', views.addTrip),
    path('travel/destination/<int:id>', views.travelInfo),
    path('join/<int:id>', views.join),
    path('leave/<int:id>', views.leave),
    path('logout', views.logout),
]