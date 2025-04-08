from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from account.models import UserModel
from account.serializers import UserSerializer

# Create your views here.

class UserAPI(ModelViewSet):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]
        
        return [IsAuthenticated()]
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return UserModel.objects.filter(id = self.request.user.id)
        
        return UserModel.objects.none()