from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='workout-home'),
    path('coding/', views.coding, name='workout-coding'),
]