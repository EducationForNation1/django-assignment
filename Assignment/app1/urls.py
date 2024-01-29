# myfeedapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('post_message/', views.post_message, name='post_message'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/create/', views.create_message, name='create_message'),
    path('messages/<int:message_id>/comment/', views.create_comment, name='create_comment'),
    path('message/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('like/message/<int:message_id>/', views.like_message, name='like_message'),
    path('like/comment/<int:comment_id>/', views.like_comment, name='like_comment'),
]
