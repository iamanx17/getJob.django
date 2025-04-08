from django.db import models
from account.models import userModel

# Create your models here.
USER_ROLE = (
    ('HR', 'HR'),
    ('ADMIN', 'admin'),
)


class companyModel(models.Model):
    company_name = models.CharField(unique=True, max_length=30)
    logo = models.ImageField(upload_to='comapny_logo/', blank=True, null=True)
    description = models.TextField()
    address = models.TextField()
    pin_code = models.PositiveIntegerField()
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(unique=True)
    linkedin_url = models.URLField(null=True, blank=True)

    added_by = models.ForeignKey(userModel, on_delete=models.CASCADE, related_name='owned_companies')
    joined_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


#to do : add users in company 
class companyUser(models.Model):
    company = models.ForeignKey(companyModel, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(userModel, on_delete=models.CASCADE)
    role = models.CharField(choices=USER_ROLE, default='HR')


    def __str__(self):
        return self.company.company_name + ' ' + self.user.email + ' ' + self.role

