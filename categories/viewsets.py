from rest_framework import permissions, viewsets

from .models import Category
from .serializers import CategorySerializer


# Create your views here.
class CategoriesViewSet(
	viewsets.ModelViewSet
):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = [permissions.AllowAny]