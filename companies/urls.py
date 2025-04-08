from rest_framework.routers import DefaultRouter
from django.urls import path, include
from companies import views


router = DefaultRouter()
router.register('', views.CompanyAPI)
router.register('addcompuser', views.CompanyUserAPI)

urlpatterns = [
    path('', include(router.urls))
]