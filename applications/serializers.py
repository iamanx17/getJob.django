from rest_framework.serializers import ModelSerializer
from applications.models import applicationModel


class applicationSerializer(ModelSerializer):
    class Meta:
        model = applicationModel
        fields = ['id', 'job', 'applicant','cover_letter', 'applied_at', 'status', 'resume']
        extra_kwargs={
            'applied_at': {'read_only': True},
            'applicant': {'read_only': True},
            'status': {'read_only': True}
        }