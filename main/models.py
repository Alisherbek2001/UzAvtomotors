from django.db import models
from django.utils.text import slugify
from common.models import BaseModel
from django.core.files.storage import default_storage

class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
     
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
        
class SubCategory(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='subcategories')
    slug = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
     
    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

class AboutCompany(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='main/about_company', blank=True, null=True)
    text = models.TextField()
    history_name = models.CharField(max_length=255)
    history = models.JSONField(default=list)

    def add_event(self, event):
        self.history.append(event)
        self.save()

    def get_history(self):
        return self.history

 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'About Company'
        verbose_name_plural = 'About Companies'


class AboutCompanyImage(BaseModel):
    about_company = models.ForeignKey(AboutCompany, related_name='company_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main/about_company/images/')

    def save(self, *args, **kwargs):
        # Yangilanish holatida eski faylni o'chirish
        if self.pk:
            try:
                old_image = AboutCompanyImage.objects.get(pk=self.pk).image
            except AboutCompanyImage.DoesNotExist:
                old_image = None
            
            if old_image and old_image != self.image:
                if default_storage.exists(old_image.name):
                    default_storage.delete(old_image.name)
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Faylni o'chirish
        if self.image and default_storage.exists(self.image.name):
            default_storage.delete(self.image.name)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'AboutCompanyImage'
        verbose_name_plural = 'AboutCompanyImages'


class GoalCompany(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='goal_companies')
    title1 = models.CharField(max_length=255)
    goal_list = models.JSONField(default=list)
    image1 = models.ImageField(upload_to='main/goal_company', blank=True, null=True)
    title2 = models.CharField(max_length=255)
    table = models.JSONField(default=list)
    image2 = models.ImageField(upload_to='main/goal_company', blank=True, null=True)
    
    def add_event(self, event):
        self.goal_list.append(event)
        self.save()

    def get_history(self):
        return self.goal_list
    
    def add_event_table(self, title, body):
        event_table = {"title": title, "body": body}
        self.table.append(event_table)
        self.save()

    def get_table(self):
        return self.table

    def save(self, *args, **kwargs):
        # Yangilanish holatida eski fayllarni o'chirish
        if self.pk:
            old_instance = GoalCompany.objects.get(pk=self.pk)
            
            # Eski rasm o'chirish
            if old_instance.image1 and old_instance.image1 != self.image1:
                if default_storage.exists(old_instance.image1.name):
                    default_storage.delete(old_instance.image1.name)

            if old_instance.image2 and old_instance.image2 != self.image2:
                if default_storage.exists(old_instance.image2.name):
                    default_storage.delete(old_instance.image2.name)

            # Eski table elementlarida rasm o'chirish
            for entry in old_instance.table:
                if 'image_url' in entry and default_storage.exists(entry['image_url']):
                    default_storage.delete(entry['image_url'])
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Rasm fayllarini o'chirish
        if self.image1 and default_storage.exists(self.image1.name):
            default_storage.delete(self.image1.name)

        if self.image2 and default_storage.exists(self.image2.name):
            default_storage.delete(self.image2.name)

        # Table elementlarida rasm o'chirish
        for entry in self.table:
            if 'image_url' in entry and default_storage.exists(entry['image_url']):
                default_storage.delete(entry['image_url'])

        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Goal Company'
        verbose_name_plural = 'Goal Companies'
        

class OurViewsCompany(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    our_views = models.CharField(max_length=255)
    our_mission = models.CharField(max_length=255)
    our_corporate_culture = models.JSONField(default=list)

    def __str__(self):
        return self.name

    def add_corporate_culture_item(self, icon, title, body):
        item = {"icon": icon, "title": title, "body": body}
        self.our_corporate_culture.append(item)
        self.save()

    def update_corporate_culture_item(self, index, icon=None, title=None, body=None):
        try:
            item = self.our_corporate_culture[index]
            if icon:
                item["icon"] = icon
            if title:
                item["title"] = title
            if body:
                item["body"] = body
            self.our_corporate_culture[index] = item
            self.save()
        except IndexError:
            raise ValueError("Invalid index")

    def remove_corporate_culture_item(self, index):
        try:
            self.our_corporate_culture.pop(index)
            self.save()
        except IndexError:
            raise ValueError("Invalid index")

    class Meta:
        verbose_name = 'Our vision and mission is our company'
        verbose_name_plural = 'Our vision and mission is our company'
        
        
class SupervisorBoardCompany(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    supervisor_board_list = models.JSONField(default=list)
    
    
    def add_supervisor(self, name, position):
        supervisor = {"name": name, "position": position}
        self.supervisor_board_list.append(supervisor)
        self.save()

    def get_supervisors(self):
        return self.supervisor_board_list

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Supervisor Board Company'
        verbose_name_plural = 'Supervisor Board Companies'
        
        
class LidershipCompany(BaseModel):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='main_lidership/company')
    experience = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'LidershipCompany'
        verbose_name_plural = 'LidershipCompanies'
    
    
class OrganizationalStructure(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_organizational/company')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Organizational Structure"
        verbose_name_plural = "Organizational Structures"
        
        
class DevelopmentStrategy(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='development_main/company/')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Development strategy"
        verbose_name_plural = "Development strategies"
        
class EnvironmentalProtectionCompany(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main_environmental/company')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Environmental Protection Privacy"
        verbose_name_plural = "Environmental Protection Privacies"
        

class EnergyManagmentSystemCompany(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main_energy/company')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Energy Managment System Policy"
        verbose_name_plural = "Energy Managment System Policies"
        
        
        
class DutiesCompany(BaseModel):
    file_name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_duties/company')
    
    def __str__(self) -> str:
        return self.file_name
    
    class Meta:
        verbose_name = "Duties of the compliance service"
        verbose_name_plural = "Duties of the compliance services"
        

class CorporateDocumentsCorporate(BaseModel):
    file_name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_corporate_documants/corporate')
    
    def __str__(self) -> str:
        return self.file_name
    
    class Meta:
        verbose_name = "Corporate Governance Document"
        verbose_name_plural = "Corporate Governance Documents"
        

class RegulationCorporate(BaseModel):
    file_name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_regulation/corporate')
    
    def __str__(self) -> str:
        return self.file_name
    
    class Meta:
        verbose_name = "Regulation"
        verbose_name_plural = "Regulations"
        
        
class ShareholdersCorporate(BaseModel):
    filename = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_regulation/corporate')
    
    def __str__(self) -> str:
        return self.filename
    
    class Meta:
        verbose_name = "MEETING OF SHAREHOLDER"
        verbose_name_plural = "MEETING OF SHAREHOLDERS"
        
class AffiliatesCorporate(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    manzili = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "LIST OF AFFILIATES"
        verbose_name_plural = "LIST OF AFFILIATES"
        

class FactsCorporate(BaseModel):
    date = models.DateField(default='2023-05-29')
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    volume = models.FloatField() 
    file = models.FileField(upload_to='main_facts/corporate')
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Important Fact"
        verbose_name_plural = "Important Facts"
        
        
class LaborProtectionCorporate(BaseModel):
    filename = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_labor/corporate')
    
    def __str__(self) -> str:
        return self.filename
    
    class Meta:
        verbose_name = "Labor protection and technical safety"
        verbose_name_plural = "Labor protection and technical safeties"
        

class DividendCorporate(BaseModel):
    year = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    calculated_dividend = models.CharField(max_length=255)
    paid_dividends = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.year
    
    class Meta:
        verbose_name = "Dividend"
        verbose_name_plural = "Dividends"
        

class ReportCorporate(BaseModel):
    filename = models.CharField(max_length=244)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_report/corporate')
    
    def __str__(self) -> str:
        return self.filename
    
    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"
    
        
class PurchasePlanCorporate(BaseModel):
    filename = models.CharField(max_length=244)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_purchase/corporate')
    
    def __str__(self) -> str:
        return self.filename
    
    class Meta:
        verbose_name = "Purchase Plan"
        verbose_name_plural = "Purchase Plans"
        

class TenderCorporate(BaseModel):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tender_id = models.IntegerField()
    price = models.FloatField()
    link = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Tender'
        verbose_name_plural = 'Tenders'
        
        
class BusinessPlanCorporate(BaseModel):
    filename = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_business/corporate')
    
    def __str__(self) -> str:
        return self.filename
    
    class Meta:
        verbose_name = 'Business Plan'
        verbose_name_plural = 'Business Plans'
        
class IssueOfSecuritiesCorporate(BaseModel):
    filename = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_security/corporate')
    
    def __str__(self) -> str:
        return self.filename
    
    class Meta:
        verbose_name = 'Issue of Security'
        verbose_name_plural = 'Issue of Securities'
    
    
class AuditorsRepotsCorporate(BaseModel):
    filename = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_auditors/corporate')
    
    def __str__(self) -> str:
        return self.filename
    
    class Meta:
        verbose_name = "Auditor's Report"
        verbose_name_plural = "Auditor's Reports"
   
   
class FinancialCorporate(BaseModel):
    filename = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_financial/corporate')
    
    def __str__(self) -> str:
        return self.filename
    
    class Meta:
        verbose_name = "Financial and Economic Status Indicator"
        verbose_name_plural = "Financial and Economic Status Indicators"     
        
        

class ResultVotingCorporate(BaseModel):
    filename = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='main_result/corporate')
    
    def __str__(self) -> str:
        return self.filename
    
    class Meta:
        verbose_name = "Result of voting"
        verbose_name_plural = "Results of voting" 
        
        
class News(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=255,null=True,blank=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.pk}) {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class NewsImage(BaseModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_images')
    image = models.ImageField(upload_to='news/news_images/')

    def __str__(self):
        return f"{self.pk}) {self.news.title}"

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "News image"
        verbose_name_plural = "News images"
        
class Engine(models.Model):
    ENGINE_TYPES = [
        ('CSS_PRIME', 'CSS PRIME'),
        ('STANDARD', 'Standart'),
    ]

    name = models.CharField(max_length=100, verbose_name="Dvigatel nomi")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/image')
    type = models.CharField(max_length=20, choices=ENGINE_TYPES, default='STANDARD', verbose_name="Dvigatel turi")
    cylinder_volume = models.FloatField(verbose_name="Silindr hajmi, L")
    cylinder_spacing = models.IntegerField(verbose_name="Silindrlar orasidagi masofa, mm")
    cylinder_diameter = models.FloatField(verbose_name="Silindr diametri, mm")
    piston_stroke = models.FloatField(verbose_name="Porshen yo'li, mm")
    compression_ratio = models.FloatField(verbose_name="Siqish darajasi")
    number_of_cylinders = models.IntegerField(verbose_name="Silindrlar soni")
    valves_per_cylinder = models.IntegerField(verbose_name="Har bir silindrdagi klapanlar soni")
    max_torque = models.FloatField(verbose_name="Maksimal aylanish momenti, Nm")
    max_power = models.FloatField(verbose_name="Maksimal quvvati, kW")
    fuel_consumption = models.FloatField(verbose_name="Yoqilg'i sarfi, L/100km")
    weight = models.FloatField(verbose_name="Dvigatel og'irligi, kg")
    dimensions = models.CharField(max_length=50, verbose_name="Dvigatel o'lchamlari (U/K/B), mm")
    emission_standard = models.CharField(max_length=20, verbose_name="Emissiya standarti")
    recommended_octane = models.IntegerField(verbose_name="Taklif qilingan benzin oktan raqami")

    def __str__(self):
        return f"{self.get_type_display()} - {self.name}"

    class Meta:
        verbose_name = "Dvigatel"
        verbose_name_plural = "Dvigatellar"
        
        
class RotationEmployee(BaseModel):
    filename = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    file = models.FileField(upload_to='rotate_main/file')
    
    def __str__(self) -> str:
        return self.filename
    
class WomanBoard(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=255,null=True,blank=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.pk}) {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "WomanBoard"
        verbose_name_plural = "WomanBoard"


class WomanBoardImage(BaseModel):
    womanboard = models.ForeignKey(WomanBoard, on_delete=models.CASCADE, related_name='womanboard_images')
    image = models.ImageField(upload_to='woman/womanboard_images/')

    def __str__(self):
        return f"{self.pk}) {self.womanboard.title}"

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "WomanBoard image"
        verbose_name_plural = "WomanBoard images"