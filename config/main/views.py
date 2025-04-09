from rest_framework import generics
from .models import Category, Foods, Comment
from .serializers import CategorySerializer, FoodsSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class FoodsListView(generics.ListCreateAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    permission_classes = [IsAdminOrReadOnly]


class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    permission_classes = [IsAdminOrReadOnly]


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly]


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        food_id = self.kwargs['food_id']
        return Comment.objects.filter(food_id=food_id)
