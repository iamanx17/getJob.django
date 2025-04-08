from rest_framework.permissions import BasePermission
from companies.models import companyUser, companyModel

class isCompanyMember(BasePermission):

    def has_permission(self, request, view):
        try:
            user = request.user
            company_name = request.data.get('company_name', None)
            if not company_name:
                return False
            
            company = companyModel.objects.get(company_name = company_name)
            
            return user.is_authenticated and companyUser.objects.filter(user = user,company=company).exists()
        
        except companyModel.DoesNotExist as err:
            print('invalid company does not exist')
            return False
        
        except Exception as e:
            print('error occured failed to create job', e)
            return False