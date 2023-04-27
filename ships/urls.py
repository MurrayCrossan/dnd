from django.urls import path
from . import views

urlpatterns = [
    path('', views.guiLoad, name="shipsHome"),
    path('newship/<slug>/', views.newShip),
    path('<slug>/', views.loadShip),
    path('testingship/', views.viewShips),
    path('testingship/<slug>/', views.testLoad)
]