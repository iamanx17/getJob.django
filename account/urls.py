from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from account import views
from django.urls import path, include

router = DefaultRouter()
router.register('',views.userAPI, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='get_access_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_access_token')
]
