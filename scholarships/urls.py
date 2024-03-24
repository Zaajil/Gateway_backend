from django.urls import path
from . import views

urlpatterns = [
    path('', views.scholarship_list, name='scholarship_list'),
    path('filter/', views.filter_scholarships, name='filter_scholarships'),
    path('add/', views.add_scholarship, name='add_scholarship'),
    path('<str:id>/', views.scholarship_detail, name='scholarship_detail'),
    path('<str:id>/edit/', views.edit_scholarship, name='edit_scholarship'),  # New path for editing scholarships
    path('<str:id>/delete/', views.delete_scholarship, name='delete_scholarship'),  # Path for deleting scholarships
]
