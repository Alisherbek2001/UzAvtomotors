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

class AboutCompany(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='about/company', blank=True, null=True)
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
    about_company = models.ForeignKey(AboutCompany, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about/company/images/')

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
    slug = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title1 = models.CharField(max_length=255)
    goal_list = models.JSONField(default=list)
    image1 = models.ImageField(upload_to='goal/company', blank=True, null=True)
    title2 = models.CharField(max_length=255)
    table = models.JSONField(default=list)
    image2 = models.ImageField(upload_to='goal/company', blank=True, null=True)
    
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
        self.slug = slugify(self.name)
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
    slug = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    our_views = models.CharField(max_length=255)
    our_mission = models.CharField(max_length=255)
    our_corporate_culture = models.JSONField(default=list)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    slug = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supervisor_board_list = models.JSONField(default=list)
    
    
    def add_supervisor(self, name, position):
        supervisor = {"name": name, "position": position}
        self.supervisor_board_list.append(supervisor)
        self.save()

    def get_supervisors(self):
        return self.supervisor_board_list

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Supervisor Board Company'
        verbose_name_plural = 'Supervisor Board Companies'
        
        
class LidershipCompany(BaseModel):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='lidership/company/')
    experience = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'LidershipCompany'
        verbose_name_plural = 'LidershipCompanies'
    