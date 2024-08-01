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
    
class PurchasePlanCorporateListAPIView(generics.ListAPIView):
    queryset = PurchasePlanCorporate.objects.all()
    serializer_class = PurchasePlanCorporateSerializer
    
class TenderCorporateListAPIView(generics.ListAPIView):
    queryset = TenderCorporate.objects.all()
    serializer_class = TenderCorporateSerializer
    
class BusinessPlanCorporateListAPIView(generics.ListAPIView):
    queryset = BusinessPlanCorporate.objects.all()
    serializer_class = BusinessPlanCorporateSerializer
    
class IssueOfSecuritiesCorporateListAPIView(generics.ListAPIView):
    queryset = IssueOfSecuritiesCorporate.objects.all()
    serializer_class = IssueOfSecuritiesCorporateSerializer
    
    
class AuditorsRepotsCorporateListAPIView(generics.ListAPIView):
    queryset = AuditorsRepotsCorporate.objects.all()
    serializer_class = AuditorsRepotsCorporateSerializer
    
class FinancialCorporateListAPIView(generics.ListAPIView):
    queryset = FinancialCorporate.objects.all()
    serializer_class = FinancialCorporateSerializer


class ResultVotingCorporateListAPIView(generics.ListAPIView):
    queryset = ResultVotingCorporate.objects.all()
    serializer_class = ResultVotingCorporateSerializer
    
class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
class ProductAPIView(generics.ListAPIView):
    queryset = Engine.objects.all()
    serializer_class = ProductsSerializer