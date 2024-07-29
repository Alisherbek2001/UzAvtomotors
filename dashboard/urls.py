from django.urls import path
from . import views

app_name = 'dash'

urlpatterns = [
    path('', views.main, name='main'),
    path('about-companies/', views.AboutCompanyView.as_view(), name='about_companies'),
    path('about-companies/delete-image/', views.AboutCompanyView.as_view(), name='aboutcompany_delete_image'),
]