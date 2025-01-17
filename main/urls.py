from django.urls import path
from .views import *

urlpatterns = [
    path('ayollar/',WomanBoardAPIView.as_view(),name='woman-list'),
    path('maxsulotlar/',ProductAPIView.as_view(),name='products-list'),
    path('yangiliklar/<int:pk>/',NewsDetailView.as_view(),name='news-detail'),
    path('yangiliklar/',NewsListAPIView.as_view(),name='news-list'),
    path('aksiyadorlarning/',ResultVotingCorporateListAPIView.as_view(),name='resultvotingcorporate-list'),
    path('moliyaviy/',FinancialCorporateListAPIView.as_view(),name='financialcorporate-list'),
    path('auditor/',AuditorsRepotsCorporateListAPIView.as_view(),name='auiditorcorporate-list'),
    path('qimmatli/',IssueOfSecuritiesCorporateListAPIView.as_view(),name='issuecorporate-list'),
    path('biznes/',BusinessPlanCorporateListAPIView.as_view(),name='businesscorporate-list'),
    path('tanlov/',TenderCorporateListAPIView.as_view(),name='tendercorporate-list'),
    path('harid/',PurchasePlanCorporateListAPIView.as_view(),name='purcahecorporate-list'),
    path('hisobotlar/',ReportCorporateListAPIView.as_view(),name='reportcorporate-list'),
    path('dividendlar/',DividendCorporateListAPIView.as_view(),name='dividendcorporate-list'),
    path('mehnat/',LaborProtectionCorporateListAPIView.as_view(),name='laborcorporate-list'),
    path('muhim/',FactsCorporateListAPIView.as_view(),name='factcorporate-list'),
    path('affiflangan/',AffiliatesCorporateListAPIView.as_view(),name="affiliatescorporate-list"),
    path('aksiyadorlar/',ShareholdersCorporateListAPIView.as_view(),name='shareholderscorporate-list'),
    path('nizom/',RegulationCorporateListAPIView.as_view()),
    path('korparativ/',CorporateDocumentsCorporateListAPIView.as_view(),name='corporatecompany-list'),
    path('komplayens/',DutiesCompanyListAPIView.as_view(),name='dutiescompany-list'),
    path('energiya/',EnergyManagmentCompanyListAPIVIew.as_view(),name='energycompany-list'),
    path('atrof/',EnvironmentalCompanyListAPIView.as_view(),name='environmental-list'),
    path('rivojlanish/',DevelopmentStrategyListAPIView.as_view(),name='development-list'),
    path('tashkiliy/',OrganizationalStructureListAPIView.as_view(),name='organizational-list'),
    path('rahbaryat/',LidershipCompanyListAPIView.as_view(),name='lidership-detail'),
    path('kuzatuv/<int:pk>/',SupervisorDetailView.as_view(),name='supervisor-detail'),
    path('qarashlarimiz/<int:pk>/',OurViewDetailView.as_view(),name='ourview-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('<slug:slug>/', AboutCompanySubCategoryDetailView.as_view(), name='aboutcompanysubcategory-detail'),
    path('goal/<slug:slug>/',GoalCompanySubCategoryDetailView.as_view(),name='goalcompany-detail')
    
]
