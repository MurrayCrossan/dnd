from django.urls import path
from . import views

urlpatterns = [
     path('', views.TableList.as_view(), name='table_list'),
     path('<slug:slug>', views.TableDetail.as_view(), name='table_detail'),
     ]