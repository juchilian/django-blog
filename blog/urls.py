from django.urls import path, re_path

from .views import (
    blog_post_create_view, 
    blog_post_detail_view, 
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view
)

app_name = 'blog'
urlpatterns = [
    path('', blog_post_list_view, name='blog_list'),
    path('<slug:slug>/', blog_post_detail_view),
    path('<slug:slug>/edit/', blog_post_update_view),
    path('<slug:slug>/delete/', blog_post_delete_view),
]
