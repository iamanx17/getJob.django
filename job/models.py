from django.db import models
from account.models import UserModel
from companies.models import CompanyModel

# Create your models here.

JOB_TYPE = (
    ('FT', 'fulltime'),
    ('C', 'contract'),
    ('IS', 'internship')
)

LOCATION_TYPE = (
    ('HB', 'Hybrid'),
    ('OS', 'onsite'),
    ('RE', 'remote')
)

class JobModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.TextField()
    job_type = models.CharField(choices=JOB_TYPE)
    location_type = models.CharField(choices=LOCATION_TYPE)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    min_salary = models.PositiveIntegerField(null=True, blank=True)
    max_salary = models.PositiveIntegerField(null=True, blank=True)
    
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='company_posted_jobs')
    posted_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posted_jobs')

    def __str__(self):
        return self.title + '' + self.job_type 
    
