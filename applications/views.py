from rest_framework.viewsets import ModelViewSet
from applications.models import applicationModel
from applications.serializers import applicationSerializer
from rest_framework.permissions import IsAuthenticated
from applications.auth import isApplicant

# Create your views here.

class applicationAPI(ModelViewSet):
    queryset = applicationModel.objects.all()
    serializer_class = applicationSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated(), isApplicant()]
        
        return [IsAuthenticated()]
