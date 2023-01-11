from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_sprinklers, name='list_sprinklers'),
    path('plan/', views.view_plans, name='list_plans')
]