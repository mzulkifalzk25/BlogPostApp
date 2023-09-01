from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = PostSerializer
