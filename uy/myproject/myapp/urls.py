from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_course/', views.create_course, name='create_course'),
    path('create_lesson/', views.create_lesson, name='create_lesson'),
    path('create_turlar/', views.create_turlar, name='create_turlar'),
    path('create_gullar/', views.create_gullar, name='create_gullar'),
    path('course_list/', views.course_list, name='course_list'),
    path('lesson_list/', views.lesson_list, name='lesson_list'),
]