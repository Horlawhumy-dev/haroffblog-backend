from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import BlogPostSerializer, BlogCategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .pagination import BlogPagination

from .models import BlogCategory, BlogPost

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    serializer_class = BlogPostSerializer
    pagination_class = BlogPagination

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    serializer_class = BlogPostSerializer


class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.filter(featured=True).order_by('-date_created')
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    serializer_class = BlogPostSerializer

class BlogPostRecentView(ListAPIView):
    queryset = BlogPost.objects.filter(recent=True).order_by('-date_created')
    # lookup_field = 'slug'
    permission_classes = [AllowAny]
    serializer_class = BlogPostSerializer

class BlogCategoryView(ListAPIView):
    queryset = BlogCategory.objects.order_by('-date_created')
    lookup_field = 'category'
    permission_classes = [AllowAny]
    serializer_class = BlogCategorySerializer

@api_view(['GET'])
def get_category(request, slug):
    if request.method == 'GET':
        cat_slug = BlogCategory.objects.get(slug=slug)
        category = BlogPost.objects.filter(category=cat_slug)
        serializer = BlogPostSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
