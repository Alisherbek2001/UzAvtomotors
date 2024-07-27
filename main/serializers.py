from rest_framework import serializers
from .models import *

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'subcategories']

class AboutCompanyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompanyImage
        fields = ['id', 'image']



class AboutCompanySerializer(serializers.ModelSerializer):
    company_images = AboutCompanyImageSerializer(many=True, read_only=True)
    class Meta:
        model = AboutCompany
        fields = ['id', 'name', 'subcategory', 'title', 'body', 'image', 'text', 'history_name', 'history','company_images']


class AboutCompanySubCategorySerializer(serializers.ModelSerializer):
    about_companies = AboutCompanySerializer(many=True, read_only=True,source='aboutcompany_set')

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'slug', 'about_companies']