from rest_framework import generics, permissions
from .models import Category, Foods, Comment
from .serializers import CategorySerializer, FoodsSerializer, CommentSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class FoodsListView(generics.ListCreateAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        food_id = self.kwargs['food_id']
        return Comment.objects.filter(food_id=food_id)