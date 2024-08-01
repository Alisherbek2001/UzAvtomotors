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
    
    
class DevelopmentStrategyListAPIView(generics.ListAPIView):
    queryset = DevelopmentStrategy.objects.all()
    serializer_class = OrganizationalCompanySerializer
    
    
class EnvironmentalCompanyListAPIView(generics.ListAPIView):
    queryset = EnvironmentalProtectionCompany.objects.all()
    serializer_class = EnvironmentalCompanySerializer
    
    
class EnergyManagmentCompanyListAPIVIew(generics.ListAPIView):
    queryset = EnergyManagmentSystemCompany.objects.all()
    serializer_class = EnvironmentalCompanySerializer
    
    
class DutiesCompanyListAPIView(generics.ListAPIView):
    queryset = DutiesCompany.objects.all()
    serializer_class = DutiesCompanySerializer
    

class CorporateDocumentsCorporateListAPIView(generics.ListAPIView):
    queryset = CorporateDocumentsCorporate.objects.all()
    serializer_class = CorporateDocumentsCorporateSerializer
    
class RegulationCorporateListAPIView(generics.ListAPIView):
    queryset = RegulationCorporate.objects.all()
    serializer_class = RegulationCorporateSerializer
    

class ShareholdersCorporateListAPIView(generics.ListAPIView):
    queryset = ShareholdersCorporate.objects.all()
    serializer_class = ShareholdersCorporateSerializer
    

class AffiliatesCorporateListAPIView(generics.ListAPIView):
    queryset = AffiliatesCorporate.objects.all()
    serializer_class = AffiliatesCorporateSerializer
    
    
class FactsCorporateListAPIView(generics.ListAPIView):
    queryset = FactsCorporate.objects.all()
    serializer_class = FactsCorporateSerializer
    
class LaborProtectionCorporateListAPIView(generics.ListAPIView):
    queryset = LaborProtectionCorporate.objects.all()
    serializer_class = LaborProtectionCorporateSerializer

class DividendCorporateListAPIView(generics.ListAPIView):
    queryset = DividendCorporate.objects.all()
    serializer_class = DividendCorporateSerializer
    
class ReportCorporateListAPIView(generics.ListAPIView):
    queryset = ReportCorporate.objects.all()
    serializer_class = ReportCorporateSerializer