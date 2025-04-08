from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from job.auth import isCompanyMember
from job.models import JobModel
from companies.models import CompanyModel
from rest_framework import status
from rest_framework.response import Response
from job.serializers import JobSerializer

# Create your views here.


class JobAPI(ModelViewSet):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = JobSerializer(data = request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            company_name = serializer.validated_data.pop('company_name')
            company = CompanyModel.objects.get(company_name = company_name)

            saved_job =serializer.save(posted_by = request.user, company = company)
            response = JobSerializer(saved_job)           
            return Response({'result': 'Job has been posted successfully', 'job': response.data})

        except CompanyModel.DoesNotExist as err:
            return Response({'error': 'Invalid company name'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get_permissions(self):
        if self.action in ['list']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), isCompanyMember()]
        
