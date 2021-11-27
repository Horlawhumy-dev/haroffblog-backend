from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView, BlogPostRecentView, BlogCategoryView,get_category 

urlpatterns = [
    path('all', BlogPostListView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    path('recent', BlogPostRecentView.as_view()),
    path('category', BlogCategoryView.as_view()),
    path('category/<slug>', get_category),
]