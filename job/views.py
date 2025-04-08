from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from job.auth import isCompanyMember
from job.models import jobModel
from companies.models import companyModel
from rest_framework import status
from rest_framework.response import Response
from job.serializers import jobSerializer

# Create your views here.


class jobAPI(ModelViewSet):
    queryset = jobModel.objects.all()
    serializer_class = jobSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = jobSerializer(data = request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            company_name = serializer.validated_data.pop('company_name')
            company = companyModel.objects.get(company_name = company_name)

            saved_job =serializer.save(posted_by = request.user, company = company)
            response = jobSerializer(saved_job)           
            return Response({'result': 'Job has been posted successfully', 'job': response.data})

        except companyModel.DoesNotExist as err:
            return Response({'error': 'Invalid company name'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated(), isCompanyMember()]
        return [IsAuthenticated()]
        
