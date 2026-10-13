from django.urls import path
from . import views

urlpatterns = [
    path('logs/', views.create_motion_log, name='create_motion_log'),
]