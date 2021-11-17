from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework.routers import SimpleRouter
from .views import CiAdminViewSet

router=SimpleRouter()
router.register('ciadmin',CiAdminViewSet,basename='ciadmin')
urlpatterns=router.urls