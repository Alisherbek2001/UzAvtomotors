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
        
        
class GoalCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalCompany
        fields = ['id','name','subcategory','title1','goal_list','image1','title2','table','image2']
        
class GoalCompanySubCategorySerializer(serializers.ModelSerializer):
    goal_companies = GoalCompanySerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'slug', 'goal_companies']   
        
        
class OurViewSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = OurViewsCompany
        fields = '__all__'
        
        
class SupervisorBoardSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = SupervisorBoardCompany
        fields = '__all__'
        
class LidershipCompanySerizalizer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = LidershipCompany
        fields = '__all__'
        
        
class OrganizationalCompanySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = OrganizationalStructure
        fields = '__all__'
        
class DevelopmentStrategyCompanySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = DevelopmentStrategy
        fields = '__all__'
        
class EnvironmentalCompanySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = EnvironmentalProtectionCompany
        fields = '__all__'
        

class EnergyManagmentCompanySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = EnergyManagmentSystemCompany
        fields = '__all__'
                

class DutiesCompanySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = DutiesCompany
        fields = '__all__'
        
class CorporateDocumentsCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = CorporateDocumentsCorporate
        fields = '__all__'
        
class RegulationCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = RegulationCorporate
        fields = '__all__'
        
class ShareholdersCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = ShareholdersCorporate
        fields = '__all__'
        
class AffiliatesCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = AffiliatesCorporate
        fields = '__all__'
        
class FactsCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = FactsCorporate
        fields = '__all__'
        

class LaborProtectionCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = LaborProtectionCorporate
        fields = '__all__'
        
class DividendCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = DividendCorporate
        fields = '__all__'
        
class ReportCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = ReportCorporate
        fields = '__all__'
        
class PurchasePlanCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = PurchasePlanCorporate
        fields = '__all__'
        
class TenderCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = TenderCorporate
        fields = '__all__'
        
        
class BusinessPlanCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = BusinessPlanCorporate
        fields = '__all__'
        
class IssueOfSecuritiesCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = IssueOfSecuritiesCorporate
        fields = '__all__'
        
class AuditorsRepotsCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = AuditorsRepotsCorporate
        fields = '__all__'
        
class FinancialCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = FinancialCorporate
        fields = '__all__'
        
class ResultVotingCorporateSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    class Meta:
        model = ResultVotingCorporate
        fields = '__all__'
        

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['id', 'image']

class NewsSerializer(serializers.ModelSerializer):
    news_images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'category', 'slug', 'body', 'news_images']

    def create(self, validated_data):
        news = News.objects.create(**validated_data)
        return news