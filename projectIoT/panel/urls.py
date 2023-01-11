from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_sprinklers, name='list_sprinklers'),
    path('<int:id>',views.delete_sprinkler, name='delete_sprinkler'),
    path('plan/', views.view_plans, name='list_plans'),
    path('plan/<int:id>', views.delete_plan, name='delete_plan')
]