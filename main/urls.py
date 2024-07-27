from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('<slug:slug>/', AboutCompanySubCategoryDetailView.as_view(), name='aboutcompanysubcategory-detail'),
    path('goal/<slug:slug>/',GoalCompanySubCategoryDetailView.as_view(),name='goalcompany-detail')
]
