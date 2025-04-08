from django.contrib import admin
from companies.models import CompanyModel, CompanyUserModel

# Register your models here.

admin.site.register(CompanyModel)
admin.site.register(CompanyUserModel)

