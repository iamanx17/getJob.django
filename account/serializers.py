from rest_framework.serializers import ModelSerializer
from account.models import userModel

class userSerializer(ModelSerializer):
    class Meta:
        model = userModel
        fields = ['id', 'first_name', 'last_name', 'api_key', 'email','user_img','owned_companies','posted_jobs',
                  'dob', 'password', 'joined_at', 'last_modified', 'user_type', 'bio', 'linkedin_url']
        extra_kwargs = {
            'joined_at': {'read_only': True},
            'last_modified': {'read_only': True},
            'api_key': {'read_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = userModel(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['owned_companies'] = len(data.get('owned_companies', []))
        data['posted_jobs'] = len(data.get('posted_jobs', []))
        return data 
