from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexList.as_view(), name="wikiHome"),
    path('Continent/<slug:slug>', views.BlogDetail, name='continent_detail'),
    path('Nation/<slug:slug>/', views.BlogDetail, name='nation_detail'),
    path('Location/<slug:slug>/', views.BlogDetail, name='location_detail'),
    path('Person/<slug:slug>/', views.BlogDetail, name='person_detail'),
    path('Item/<slug:slug>/', views.BlogDetail, name='item_detail'),
    path('Organisation/<slug:slug>/', views.BlogDetail, name='organisation_detail'),
    path('seats/', views.seats)
]