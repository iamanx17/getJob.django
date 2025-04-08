from django.db.models.signals import post_save
from django.dispatch import receiver
from companies.models import companyUser, companyModel



@receiver(post_save, sender = companyModel)
def add_creat_company_group(sender, instance, created, **kwarggs):
    if created:
        companyUser.objects.get_or_create(
            company = instance,
            user = instance.added_by,
            defaults={'role': 'ADMIN'}
        )