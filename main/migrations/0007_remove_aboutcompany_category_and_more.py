# Generated by Django 5.0.7 on 2024-07-25 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_organizationalstructure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutcompany',
            name='category',
        ),
        migrations.RemoveField(
            model_name='aboutcompany',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='goalcompany',
            name='category',
        ),
        migrations.RemoveField(
            model_name='goalcompany',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='organizationalstructure',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='ourviewscompany',
            name='category',
        ),
        migrations.RemoveField(
            model_name='ourviewscompany',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='supervisorboardcompany',
            name='category',
        ),
        migrations.RemoveField(
            model_name='supervisorboardcompany',
            name='slug',
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main/about_company'),
        ),
        migrations.AlterField(
            model_name='aboutcompanyimage',
            name='about_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_images', to='main.aboutcompany'),
        ),
        migrations.AlterField(
            model_name='aboutcompanyimage',
            name='image',
            field=models.ImageField(upload_to='main/about_company/images/'),
        ),
        migrations.AlterField(
            model_name='goalcompany',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='main/goal_company'),
        ),
        migrations.AlterField(
            model_name='goalcompany',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='main/goal_company'),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goalcompany',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lidershipcompany',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationalstructure',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ourviewscompany',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supervisorboardcompany',
            name='subcategory',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory'),
            preserve_default=False,
        ),
    ]
