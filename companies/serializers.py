from rest_framework.serializers import ModelSerializer
from companies.models import companyModel, companyUser
from account.models import userModel


class comapnySerializer(ModelSerializer):
    class Meta:
        model = companyModel
        fields = ['id', 'company_name', 'description', 'address', 'pin_code','company_posted_jobs',
                  'website', 'email', 'added_by', 'joined_at', 'last_modified', 'linkedin_url']
        extra_kwargs = {
            'added_by': {'read_only': True},
            'joined_at': {'read_only': True},
            'last_modified':{'read_only': True}
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['company_posted_jobs'] = len(data.get('company_posted_jobs', []))
        try:

            user_id = data.get('added_by')
            if user_id:
                user = userModel.objects.get(id = user_id)
                data['added_by'] = user.email
        except userModel.DoesNotExist as err:
            print('error occured: user not found', err)

        return data

class companyUserSerializer(ModelSerializer):
    class Meta:
        model = companyUser
        fields = ['id', 'company', 'user', 'role']