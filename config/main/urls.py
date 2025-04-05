from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    FoodsListView, FoodDetailView,
    CommentCreateView, CommentListView
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),

    path('foods/', FoodsListView.as_view()),
    path('foods/<int:pk>/', FoodDetailView.as_view()),

    path('comments/<int:food_id>/', CommentListView.as_view()),
    path('comments/create/', CommentCreateView.as_view()),
]