# knowledgebase/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example for index view  # Ensure this line is present
    path('register/', views.register, name='register'),
    path('table_view/', views.table_view, name='table_view'),
    # Other URL patterns
]
