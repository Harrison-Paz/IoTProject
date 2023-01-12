from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_sprinklers, name='list_sprinklers'),
    path('<int:id>/',views.delete_sprinkler, name='delete_sprinkler'),
    path('plan/', views.view_plans, name='list_plans'),
    path('plan/<int:id>/', views.delete_plan, name='delete_plan'),
    path('start/<int:id>/', views.start_sprinkler, name='start_sprinkler'),
    path('stop/<int:id>/', views.stop_sprinkler, name='stop_sprinkler'),
    path('edit/', views.edit_sprinkler, name='edit_sprinkler'),
]