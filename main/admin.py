from django.contrib import admin
from .models import AboutCompany, Category, AboutCompanyImage, GoalCompany,OurViewsCompany, SupervisorBoardCompany,LidershipCompany
from django import forms

class AboutCompanyImageInline(admin.TabularInline):
    model = AboutCompanyImage
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10

admin.site.register(Category, CategoryAdmin)

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
    list_display = ['name', 'title', 'category']
    search_fields = ['name', 'title']
    list_filter = ['category']

admin.site.register(AboutCompany, AboutCompanyAdmin)


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
    list_display = ['name', 'title1', 'category']
    search_fields = ['name', 'title1']
    list_filter = ['category']

admin.site.register(GoalCompany, GoalCompanyAdmin)



class OurViewsCompanyAdminForm(forms.ModelForm):
    class Meta:
        model = OurViewsCompany
        fields = '__all__'
        widgets = {
            'our_corporate_culture': forms.Textarea(attrs={'rows': 5}),
        }

class OurViewsCompanyAdmin(admin.ModelAdmin):
    form = OurViewsCompanyAdminForm
    list_display = ['name', 'our_views', 'our_mission', 'category']
    search_fields = ['name', 'our_views', 'our_mission']
    list_filter = ['category']

admin.site.register(OurViewsCompany, OurViewsCompanyAdmin)



class SupervisorBoardCompanyAdminForm(forms.ModelForm):
    class Meta:
        model = SupervisorBoardCompany
        fields = '__all__'
        widgets = {
            'supervisor_board_list': forms.Textarea(attrs={'rows': 5}),
        }

class SupervisorBoardCompanyAdmin(admin.ModelAdmin):
    form = SupervisorBoardCompanyAdminForm
    list_display = ['name', 'category']
    search_fields = ['name']
    list_filter = ['category']

admin.site.register(SupervisorBoardCompany, SupervisorBoardCompanyAdmin)


class LidershipCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'experience']
    search_fields = ['name', 'position']
    list_filter = ['position']

admin.site.register(LidershipCompany, LidershipCompanyAdmin)
