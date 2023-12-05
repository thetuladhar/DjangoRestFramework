from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

class BlogListCreateView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #pagination_class = LargeResultsSetPagination


# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000