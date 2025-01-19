from django.urls import path
from . import views

app_name = 'service_requests'

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('create/', views.request_create, name='request_create'),
    path('<int:pk>/', views.request_detail, name='request_detail'),
    path('<int:pk>/edit/', views.request_update, name='request_update'),
    path('manage/', views.manage_requests, name='manage_requests'),
    path('create/', views.request_create, name='request_create'),
]
