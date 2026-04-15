from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks),
    path('tasks/add/', views.add_task),
    path('tasks/update/<int:id>/', views.update_task),
    path('tasks/delete/<int:id>/', views.delete_task),
]