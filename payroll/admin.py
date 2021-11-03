from django.contrib import admin
from .models import Employee,ActivityLog,LoginAttempts
# Register your models here.

admin.site.register(Employee)
admin.site.register(LoginAttempts)
admin.site.register(ActivityLog)

