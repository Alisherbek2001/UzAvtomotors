from django.urls import path
from .views import *

urlpatterns = [
    path('tashkiliy/',OrganizationalStructureListAPIView.as_view(),name='organizational-list'),
    path('rahbaryat/',LidershipCompanyListAPIView.as_view(),name='lidership-detail'),
    path('kuzatuv/<int:pk>/',SupervisorDetailView.as_view(),name='supervisor-detail'),
    path('qarashlarimiz/<int:pk>/',OurViewDetailView.as_view(),name='ourview-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('<slug:slug>/', AboutCompanySubCategoryDetailView.as_view(), name='aboutcompanysubcategory-detail'),
    path('goal/<slug:slug>/',GoalCompanySubCategoryDetailView.as_view(),name='goalcompany-detail')
    
]
