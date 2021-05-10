from django.urls import path

from BLOG_POSTS import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('view/<int:blognum>', views.blog_view, name='blog_view'),
    path('create', views.blog_create, name='blog_create'),
    path('update/<int:blognum>', views.blog_update, name='blog_update'),
    path('delete/<int:blognum>', views.blog_delete, name='blog_delete'),
]
