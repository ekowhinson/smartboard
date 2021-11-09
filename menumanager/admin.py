from django.contrib import admin

from menumanager.models import MenuGroup,MenuSubGroup,MenuSubGroupDetail,DaUsers,MenuSubUsers
# Register your models here.
admin.site.register(MenuGroup)
admin.site.register(MenuSubGroup)
admin.site.register(MenuSubGroupDetail)
admin.site.register(DaUsers)
admin.site.register(MenuSubUsers)


