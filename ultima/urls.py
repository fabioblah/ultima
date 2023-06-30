from django.urls import path
from . import views

urlpatterns = [
    path('reserve_bath/', views.reserve_bath, name='reserve_bath'),
    path('reserve_success/', views.reserve_success, name='reserve_success'),
]
