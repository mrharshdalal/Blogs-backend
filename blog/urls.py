from django.urls import path
from . import views

urlpatterns = [
    path('createblog/', views.create_blog_post, name='blogpost-list'),
]
