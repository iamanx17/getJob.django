from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from account.models import userModel
from account.serializers import userSerializer

# Create your views here.

class userAPI(ModelViewSet):
    serializer_class = userSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]
        
        return [IsAuthenticated()]
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return userModel.objects.filter(id = self.request.user.id)
        
        return userModel.objects.none()