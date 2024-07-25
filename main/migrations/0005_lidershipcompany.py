# Generated by Django 5.0.7 on 2024-07-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_supervisorboardcompany'),
    ]

    operations = [
        migrations.CreateModel(
            name='LidershipCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='lidership/company/')),
                ('experience', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'LidershipCompany',
                'verbose_name_plural': 'LidershipCompanies',
            },
        ),
    ]
