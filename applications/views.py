from rest_framework.viewsets import ModelViewSet
from applications.models import ApplicationModel
from applications.serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from applications.auth import isApplicant

# Create your views here.

class ApplicationAPI(ModelViewSet):
    queryset = ApplicationModel.objects.all()
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated(), isApplicant()]
        
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(applicant = self.request.user)
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ApplicationModel.objects.filter(applicant = self.request.user)
        
        return ApplicationModel.objects.none()

        
