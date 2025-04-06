from rest_framework.routers import DefaultRouter
from django.urls import path, include
from job import views

router = DefaultRouter()
router.register('', views.jobAPI)


urlpatterns = [
    path('', include(router.urls))
]