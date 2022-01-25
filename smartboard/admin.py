from msilib.schema import Class
from django.contrib import admin
from . import models as smbmodels
# Register your models here.
admin.site.register(smbmodels.School)
admin.site.register(smbmodels.Section)
admin.site.register(smbmodels.Student)
admin.site.register(smbmodels.Subject)
admin.site.register(smbmodels.AcademicYear)
admin.site.register(smbmodels.Invoice)
admin.site.register(smbmodels.Parent)
admin.site.register(smbmodels.Teacher)
admin.site.register(smbmodels.Classes)
admin.site.register(smbmodels.ClassGroup)
admin.site.register(smbmodels.ClassSubject)
