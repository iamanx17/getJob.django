from rest_framework.serializers import ModelSerializer
from companies.models import CompanyModel, CompanyUserModel
from account.models import UserModel


class ComapnySerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ['id', 'company_name', 'description', 'address', 'pin_code','company_posted_jobs',
                  'website', 'email', 'added_by', 'joined_at', 'last_modified', 'linkedin_url']
        extra_kwargs = {
            'added_by': {'read_only': True},
            'joined_at': {'read_only': True},
            'last_modified':{'read_only': True},
            "company_posted_jobs": {'read_only': True}
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['company_posted_jobs'] = len(data.get('company_posted_jobs', []))
        try:

            user_id = data.get('added_by')
            if user_id:
                user = UserModel.objects.get(id = user_id)
                data['added_by'] = user.email
        except UserModel.DoesNotExist as err:
            print('error occured: user not found', err)

        return data

class CompanyUserSerializer(ModelSerializer):
    class Meta:
        model = CompanyUserModel
        fields = ['id', 'company', 'user', 'role']