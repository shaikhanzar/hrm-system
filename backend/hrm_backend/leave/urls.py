from django.urls import path
from . import views

urlpatterns = [
    path('leave/', views.get_leave),
    path('leave/add/', views.add_leave),
    path('leave/update/<int:id>/', views.update_leave),
    path('leave/delete/<int:id>/', views.delete_leave),
]