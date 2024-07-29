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
    
    
class OurViewDetailView(generics.RetrieveAPIView):
    queryset = OurViewsCompany.objects.all()
    serializer_class = OurViewSerializer
    
    
class SupervisorDetailView(generics.RetrieveAPIView):
    queryset = SupervisorBoardCompany.objects.all()
    serializer_class = SupervisorBoardSerializer
    
    
class LidershipCompanyListAPIView(generics.ListAPIView):
    queryset = LidershipCompany.objects.all()
    serializer_class = LidershipCompanySerizalizer
    

class OrganizationalStructureListAPIView(generics.ListAPIView):
    queryset = OrganizationalStructure.objects.all()
    serializer_class = OrganizationalCompanySerializer
    
    
    
    