from django.shortcuts import render
from rest_framework import generics
from .models import BookModel,AuthorModel
from .serializers import BookModelSerializer,AuthorModelSerializer,SocialMediaHandleSerializer




class BookListCreateView(generics.ListCreateAPIView):
    queryset=BookModel.objects.all()
    serializer_class=BookModelSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset=AuthorModel.objects.all()
    serializer_class=AuthorModelSerializer