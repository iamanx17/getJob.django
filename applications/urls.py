from rest_framework.routers import DefaultRouter
from django.urls import path, include
from applications import views

router = DefaultRouter()
router.register('', views.applicationAPI)


urlpatterns = [
    path('', include(router.urls))
]