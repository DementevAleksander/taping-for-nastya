from django.urls import path
from . import views


app_name = 'about'

urlpatterns = [
    path('author/', views.aboutauthorview, name='author'),
]
