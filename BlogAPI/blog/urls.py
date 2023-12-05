from django.urls import path
from .views import BlogListCreateView, BlogDetailView, CommentListCreateView
#,CommentListView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/<int:blog_id>/comment/', CommentListCreateView.as_view(), name='comment-list'),
]