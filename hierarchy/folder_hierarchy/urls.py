from django.urls import path
# from .views import PostByCategoryView
from . import views

# app_name = 'folder_hierarchy'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', CategoryListView.as_view(), name='category-list'),
    # path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
    path('<str:slug>/', views.group_posts, name='post-by-category'),
]
