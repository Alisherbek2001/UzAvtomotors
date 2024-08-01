# Generated by Django 5.0.7 on 2024-07-29 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_developmentstrategy'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentalProtectionCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='main_environmental/company')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subcategory')),
            ],
            options={
                'verbose_name': 'Environmental Protection Privacy',
                'verbose_name_plural': 'Environmental Protection Privacies',
            },
        ),
    ]