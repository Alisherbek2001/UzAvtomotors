# Generated by Django 5.0.7 on 2024-07-27 00:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_engine_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RotationEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('filename', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='rotate_main/file')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
