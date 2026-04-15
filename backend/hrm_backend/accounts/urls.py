from django.urls import path
from . import views

urlpatterns = [
    # Role
    path('roles/', views.get_roles),
    path('roles/add/', views.add_role),
    path('roles/delete/<int:id>/', views.delete_role),

    # User
    path('users/', views.get_users),
    path('users/add/', views.add_user),
    path('users/update/<int:id>/', views.update_user),
    path('users/delete/<int:id>/', views.delete_user),
]