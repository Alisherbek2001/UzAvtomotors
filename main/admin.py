from django.contrib import admin
from django.apps import apps
from .models import *
from django import forms

def safe_register(model, admin_class=None):
    try:
        if isinstance(model, (list, tuple)):
            for m in model:
                admin.site.register(m, admin_class)
        else:
            admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
class AboutCompanyImageInline(admin.TabularInline):
    model = AboutCompanyImage
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10

safe_register(Category, CategoryAdmin)

class AboutCompanyAdminForm(forms.ModelForm):
    class Meta:
        model = AboutCompany
        fields = '__all__'
        widgets = {
            'history': forms.Textarea(attrs={'rows': 3}),
        }

class AboutCompanyAdmin(admin.ModelAdmin):
    form = AboutCompanyAdminForm
    inlines = [AboutCompanyImageInline]
    list_display = ['name', 'title', 'subcategory']
    search_fields = ['name', 'title']
    list_filter = ['subcategory']

safe_register(AboutCompany, AboutCompanyAdmin)

class GoalCompanyAdminForm(forms.ModelForm):
    class Meta:
        model = GoalCompany
        fields = '__all__'
        widgets = {
            'goal_list': forms.Textarea(attrs={'rows': 3}),
            'table': forms.Textarea(attrs={'rows': 5}),
        }

class GoalCompanyAdmin(admin.ModelAdmin):
    form = GoalCompanyAdminForm
    list_display = ['name', 'title1', 'subcategory']
    search_fields = ['name', 'title1']
    list_filter = ['subcategory']

safe_register(GoalCompany, GoalCompanyAdmin)

class OurViewsCompanyAdminForm(forms.ModelForm):
    class Meta:
        model = OurViewsCompany
        fields = '__all__'
        widgets = {
            'our_corporate_culture': forms.Textarea(attrs={'rows': 5}),
        }

class OurViewsCompanyAdmin(admin.ModelAdmin):
    form = OurViewsCompanyAdminForm
    list_display = ['name', 'our_views', 'our_mission', 'subcategory']
    search_fields = ['name', 'our_views', 'our_mission']
    list_filter = ['subcategory']

safe_register(OurViewsCompany, OurViewsCompanyAdmin)

class SupervisorBoardCompanyAdminForm(forms.ModelForm):
    class Meta:
        model = SupervisorBoardCompany
        fields = '__all__'
        widgets = {
            'supervisor_board_list': forms.Textarea(attrs={'rows': 5}),
        }

class SupervisorBoardCompanyAdmin(admin.ModelAdmin):
    form = SupervisorBoardCompanyAdminForm
    list_display = ['name', 'subcategory']
    search_fields = ['name']
    list_filter = ['subcategory']

safe_register(SupervisorBoardCompany, SupervisorBoardCompanyAdmin)

class LidershipCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'experience']
    search_fields = ['name', 'position']
    list_filter = ['position']

safe_register(LidershipCompany, LidershipCompanyAdmin)

class OrganizationalStructureAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

safe_register(OrganizationalStructure, OrganizationalStructureAdmin)
safe_register(SubCategory)


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline]
    list_display = ['title', 'category', 'slug']
    search_fields = ['title', 'category__name']
    list_filter = ['category']

safe_register(News, NewsAdmin)


admin.site.register(AffiliatesCorporate)
admin.site.register(AuditorsRepotsCorporate)
admin.site.register(BusinessPlanCorporate)
admin.site.register(CorporateDocumentsCorporate)
admin.site.register(DividendCorporate)
admin.site.register(DutiesCompany)
admin.site.register(FactsCorporate)
admin.site.register(FinancialCorporate)
admin.site.register(IssueOfSecuritiesCorporate)
admin.site.register(LaborProtectionCorporate)
admin.site.register(PurchasePlanCorporate)
admin.site.register(RegulationCorporate)
admin.site.register(ReportCorporate)
admin.site.register(ResultVotingCorporate)
admin.site.register(ShareholdersCorporate)
admin.site.register(TenderCorporate)
admin.site.register(DevelopmentStrategy)

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'cylinder_volume', 'max_power', 'fuel_consumption')
    list_filter = ('type', 'number_of_cylinders', 'emission_standard')
    search_fields = ('name', 'type')
    
admin.site.register(RotationEmployee)