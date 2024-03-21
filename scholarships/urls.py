from django.urls import path
from . import views

urlpatterns = [
    path('', views.scholarship_list, name='scholarship_list'),
    path('filter/', views.filter_scholarships, name='filter_scholarships'),
    path('add/', views.add_scholarship, name='add_scholarship'),  # Add path for filtered scholarships
]
