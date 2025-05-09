from rest_framework import serializers
from job.models import JobModel
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(write_only=True)
    class Meta:
        model = JobModel
        fields = [
            'id', 'title', 'description','location','job_type','location_type',
            'posted_at','min_salary','max_salary','company_name','company', 'posted_by'
        ]
        extra_kwargs = {
            'posted_at': {'read_only': True},
            'posted_by': {'read_only': True},
            'company': {'read_only': True},
        }
