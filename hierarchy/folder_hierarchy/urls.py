from django.urls import path
from . import views

# app_name = 'folder_hierarchy'

urlpatterns = [
    path('', views.index, name='index'),
    path('course-content/', views.сourse_content, name='course_content'),
    path('<str:slug>/', views.group_posts, name='post-by-category'),
]
