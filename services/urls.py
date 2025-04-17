from django.urls import path
from . import views

urlpatterns = [
    path('service/<int:id>/', views.service_detail, name='service_detail'),



]