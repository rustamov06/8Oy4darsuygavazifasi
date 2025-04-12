from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Foods, Category, Comment
from .serializers import FoodsSerializer, CategorySerializer, CommentSerializer

class FoodsListView(APIView):
    def get(self, request):
        foods = Foods.objects.all()
        serializer = FoodsSerializer(foods, many=True)
        return Response(serializer.data)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CommentListView(APIView):
    def get(self, request, food_id):
        comments = Comment.objects.filter(food_id=food_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
