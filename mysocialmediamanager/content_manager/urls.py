from django.urls import path
from .views import create_post

urlpatterns = [
    path('create/', create_post, name='create_post'),  # URL for creating a post
    # path('dashboard/', dashboard, name='dashboard'),  # URL to view the dashboard or post statuses
]
