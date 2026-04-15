from django.urls import path
from . import views

urlpatterns = [
    path('performance/', views.get_performance),
    path('performance/add/', views.add_performance),
    path('performance/delete/<int:id>/', views.delete_performance)
]