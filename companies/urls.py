from rest_framework.routers import DefaultRouter
from django.urls import path, include
from companies import views


router = DefaultRouter()
router.register('', views.companyAPI)
router.register('addcompuser', views.companyUserAPI)

urlpatterns = [
    path('', include(router.urls))
]