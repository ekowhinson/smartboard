from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework.routers import SimpleRouter
from .views import ModuleViewSet,CiAdminRolesViewSet, CiAdminViewSet

router=SimpleRouter()
router.register('ciadmin',CiAdminViewSet,basename='ciadmin')
router.register('ciadminroles',CiAdminRolesViewSet,basename='ciadminroles')
router.register('modules',ModuleViewSet,basename='modules')
urlpatterns=router.urls