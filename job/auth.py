from rest_framework.permissions import BasePermission
from companies.models import CompanyUserModel, CompanyModel

class isCompanyMember(BasePermission):

    def has_permission(self, request, view):
        try:
            user = request.user
            company_name = request.data.get('company_name', None)
            if not company_name:
                return False
            
            company = CompanyModel.objects.get(company_name = company_name)
            
            return user.is_authenticated and CompanyUserModel.objects.filter(user = user,company=company).exists()
        
        except CompanyModel.DoesNotExist as err:
            print('invalid company does not exist')
            return False
        
        except Exception as e:
            print('error occured failed to create job', e)
            return False