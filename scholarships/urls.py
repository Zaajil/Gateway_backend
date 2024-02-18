from django.urls import path
from . import views

urlpatterns = [
     path('scholarship/', views.view, name='scholarship_list'),
]