from django.db.models.signals import post_save
from django.dispatch import receiver
from companies.models import CompanyUserModel, CompanyModel



@receiver(post_save, sender = CompanyModel)
def add_creat_company_group(sender, instance, created, **kwarggs):
    if created:
        CompanyUserModel.objects.get_or_create(
            company = instance,
            user = instance.added_by,
            defaults={'role': 'ADMIN'}
        )