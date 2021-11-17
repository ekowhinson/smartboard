from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import MenuGroupViewSet,MenuSubGroupDetailViewSet,MenuSubGroupViewSet,MenuSubUsersViewSet,DaUsersViewSet,UsersPermissionViewSet

router=SimpleRouter()
router.register('menugroup',MenuGroupViewSet,basename='menugroup')
router.register('menusubgroup',MenuSubGroupViewSet,basename='menusubgroup')
router.register('menusubgroupdetail',MenuSubGroupDetailViewSet,basename='menusubgroupdetail')
router.register('menusubusers',MenuSubUsersViewSet,basename='menusubusers')
router.register('dausers',DaUsersViewSet,basename='dausers')
router.register('userpermission',UsersPermissionViewSet,'userpermission')

urlpatterns=router.urls
