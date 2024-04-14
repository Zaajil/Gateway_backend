from django.urls import path
from . import views

urlpatterns = [
    path('', views.scholarship_list, name='scholarship_list'),  # List all scholarships
    path('filter/', views.filter_scholarships, name='filter_scholarships'),  # Filter scholarships
    path('add/', views.add_scholarship, name='add_scholarship'),  # Add a new scholarship
    path('<str:id>/', views.scholarship_detail, name='scholarship_detail'),  # Get details of a scholarship
    path('<str:id>/edit/', views.edit_scholarship, name='edit_scholarship'),  # Edit a scholarship
    path('<str:id>/delete/', views.delete_scholarship, name='delete_scholarship'),  # Delete a scholarship
]
