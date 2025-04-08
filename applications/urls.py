from rest_framework.routers import DefaultRouter
from django.urls import path, include
from applications import views

router = DefaultRouter()
router.register('', views.ApplicationAPI)


urlpatterns = [
    path('', include(router.urls))
]