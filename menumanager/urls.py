from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import MenuUserElementViewSet,MenuSubUsersDelete,MenuGroupViewSet,MenuSubGroupDetailViewSet,MenuSubGroupViewSet,MenuSubUsersViewSet,DaUsersViewSet,UsersPermissionViewSet

router=SimpleRouter()
router.register('menusubusersdelete',MenuSubUsersDelete,basename='menusubusersdelete')
router.register('menugroup',MenuGroupViewSet,basename='menugroup')
router.register('menusubgroup',MenuSubGroupViewSet,basename='menusubgroup')
router.register('menusubgroupdetail',MenuSubGroupDetailViewSet,basename='menusubgroupdetail')
router.register('menusubusers',MenuSubUsersViewSet,basename='menusubusers')
router.register('dausers',DaUsersViewSet,basename='dausers')
router.register('userpermission',UsersPermissionViewSet,'userpermission')
router.register('menuuserelement',MenuUserElementViewSet,basename='menuuserelement')

urlpatterns=router.urls
