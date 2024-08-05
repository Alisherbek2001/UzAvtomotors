from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from main import models


def main(request):
    return render(request, 'index.html')


# class AboutCompanyView(View):
    
#     def get(self, request, *args, **kwargs):
#         company = models.AboutCompany.objects.order_by('-created_at').first()
#         images = models.AboutCompanyImage.objects.all()
#         return render(request, 'pages/kompaniya/kompaniya-haqida/index.html', {'company': company, 'images': images})

#     def post(self, request, *args, **kwargs):
#         form = models.AboutCompanyForm(request.POST, request.FILES)
#         if form.is_valid():
#             company = form.save()
#             # Обработка изображений, если они включены в запрос
#             image_form = models.AboutCompanyImageForm(request.POST, request.FILES)
#             if image_form.is_valid():
#                 image_instance = image_form.save(commit=False)
#                 image_instance.about_company = company
#                 image_instance.save()
#             return redirect('aboutcompany_list')
#         else:
#             image_form = models.AboutCompanyImageForm()  # Пустая форма изображения для отображения
#         companies = models.AboutCompany.objects.all()
#         return render(request, self.template_name, {
#             'form': form,
#             'companies': companies,
#             'image_form': image_form
#         })

#     def put(self, request, *args, **kwargs):
#         company_id = request.POST.get('company_id')
#         company = get_object_or_404(models.AboutCompany, pk=company_id)
#         form = models.AboutCompanyForm(request.POST, request.FILES, instance=company)
#         if form.is_valid():
#             form.save()
#             return redirect('aboutcompany_list')
#         companies = models.AboutCompany.objects.all()
#         image_form = models.AboutCompanyImageForm()
#         return render(request, self.template_name, {
#             'form': form,
#             'companies': companies,
#             'image_form': image_form
#         })

#     def delete(self, request, *args, **kwargs):
#         company_id = request.POST.get('company_id')
#         company = get_object_or_404(models.AboutCompany, pk=company_id)
#         company.delete()
#         return redirect('aboutcompany_list')

#     def delete_image(self, request, *args, **kwargs):
#         image_id = request.POST.get('image_id')
#         image = get_object_or_404(models.AboutCompanyImage, pk=image_id)
#         image.delete()
#         return redirect('aboutcompany_list')