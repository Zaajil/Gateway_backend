from django.urls import path
from . import views

urlpatterns = [
    # Paths for notice-related views
    path('notice/', views.notice_list, name='notice_list'),
    path('notice/add/', views.add_notice, name='add_notice'),
    path('notice/<str:id>/edit/', views.edit_notice, name='edit_notice'),
    path('notice/<str:id>/delete/', views.delete_notice, name='delete_notice'),
]