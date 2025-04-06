from rest_framework.viewsets import ModelViewSet
from companies.serializers import comapnySerializer, companyUserSerializer
from companies.models import companyModel, companyUser
from rest_framework.permissions import IsAuthenticated
from companies.auth import isRecuriter
# Create your views here.



class companyAPI(ModelViewSet):
    queryset = companyModel.objects.all()
    serializer_class = comapnySerializer

    def get_permissions(self):
        if self.action in ['list']:
            return [IsAuthenticated()]
        
        return [IsAuthenticated(), isRecuriter()]
    
    def perform_create(self, serializer):
        serializer.save(added_by = self.request.user)
    

class companyUserAPI(ModelViewSet):
    queryset = companyUser.objects.all()
    serializer_class = companyUserSerializer
