from django.urls import path

from . import views

app_name = 'service_checker'

urlpatterns = [
    path('status/<str:service_name>', views.check_status, name='status'),
    path('dashboard', views.dashboard, name='dashboard')
]
