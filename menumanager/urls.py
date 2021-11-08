from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import MenuGropuViewSet

router=SimpleRouter()
router.register('menugroup',MenuGropuViewSet,basename='menugroup')

urlpatterns=router.urls
