# Generated by Django 5.2 on 2025-04-08 09:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='comapny_logo/')),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('pin_code', models.PositiveIntegerField()),
                ('website', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('HR', 'HR'), ('ADMIN', 'admin')], default='HR')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='companies.companymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
