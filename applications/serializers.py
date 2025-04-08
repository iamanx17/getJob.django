from rest_framework.serializers import ModelSerializer
from applications.models import ApplicationModel


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = ['id', 'job', 'applicant','cover_letter', 'applied_at', 'status', 'resume']
        extra_kwargs={
            'applied_at': {'read_only': True},
            'applicant': {'read_only': True},
            'status': {'read_only': True}
        }