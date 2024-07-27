from rest_framework import generics
from .models import *
from .serializers import *

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AboutCompanySubCategoryDetailView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = AboutCompanySubCategorySerializer
    lookup_field = 'slug'
    
    
class GoalCompanySubCategoryDetailView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = GoalCompanySubCategorySerializer
    lookup_field = 'slug'