from rest_framework.viewsets import ModelViewSet
from companies.serializers import ComapnySerializer, CompanyUserSerializer
from companies.models import CompanyModel, CompanyUserModel
from rest_framework.permissions import IsAuthenticated
from companies.auth import isRecuriter
# Create your views here.



class CompanyAPI(ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = ComapnySerializer

    def get_permissions(self):
        if self.action in ['list']:
            return [IsAuthenticated()]
        
        return [IsAuthenticated(), isRecuriter()]
    
    def perform_create(self, serializer):
        serializer.save(added_by = self.request.user)
    

class CompanyUserAPI(ModelViewSet):
    queryset = CompanyUserModel.objects.all()
    serializer_class = CompanyUserSerializer
