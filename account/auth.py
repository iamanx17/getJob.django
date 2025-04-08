from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from account.models import UserModel



class apiKeyJwtAuthentiation(BaseAuthentication):
    
    def authenticate(self, request):
        authorization = request.headers.get('Authorization')

        if not authorization:
            return None
        
        if 'Bearer'.lower() in authorization.lower():
            try:
                return JWTAuthentication().authenticate(request)
            
            except Exception as e:
                raise AuthenticationFailed('Invalid jwt token')

        try:
            user = UserModel.objects.get(api_key = authorization)
            return (user, None)
        
        except UserModel.DoesNotExist as err:
            raise AuthenticationFailed('Invalid API key')