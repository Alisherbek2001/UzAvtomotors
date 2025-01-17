# Generated by Django 5.0.7 on 2024-07-25 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('title1', models.CharField(max_length=255)),
                ('goal_list', models.JSONField(default=list)),
                ('image1', models.ImageField(upload_to='goal/company')),
                ('title2', models.CharField(max_length=255)),
                ('table', models.JSONField(default=list)),
                ('image2', models.ImageField(upload_to='goal/company')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
