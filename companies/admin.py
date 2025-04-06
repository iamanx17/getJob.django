from django.contrib import admin
from companies.models import companyModel, companyUser

# Register your models here.

admin.site.register(companyModel)
admin.site.register(companyUser)

