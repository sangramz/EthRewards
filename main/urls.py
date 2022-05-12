from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainView, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
