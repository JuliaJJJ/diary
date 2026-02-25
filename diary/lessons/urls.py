from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_lesson, name='create_lesson'),
    path('', views.all_lessons, name='all_lessons'),
    path('attendance/<int:lesson_id>/', views.mark_attendance, name='mark_attendance'),
]