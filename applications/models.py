from django.db import models
from account.models import UserModel
from job.models import JobModel
# Create your models here.

STATUS = (
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('rejected', 'rejected')
)



class ApplicationModel(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    cover_letter = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='applications/', blank=True, null=True)
    status = models.CharField(choices=STATUS, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant.email + ' ' + self.status


    

