from django.contrib import admin

from compapp.models import CiAdmin, CiAdminRoles, Module

# Register your models here.
admin.site.register(CiAdmin)
admin.site.register(CiAdminRoles)
admin.site.register(Module)