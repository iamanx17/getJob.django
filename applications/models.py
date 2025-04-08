from django.db import models
from account.models import userModel
from job.models import jobModel
# Create your models here.

STATUS = (
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('rejected', 'rejected')
)



class applicationModel(models.Model):
    job = models.ForeignKey(jobModel, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(userModel, on_delete=models.CASCADE)
    cover_letter = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='applications/', blank=True, null=True)
    status = models.CharField(choices=STATUS, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant.email + ' ' + self.status


    

