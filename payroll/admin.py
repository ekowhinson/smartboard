from django.contrib import admin
from .models import Affordability, Employee,ActivityLog,LoginAttempts,Company,CompanyBranch, Mandate, Payment,Bank,BankBranch,Element,ElementGroup,ElementCategory,TesterTable
# Register your models here.

admin.site.register(Employee)
admin.site.register(LoginAttempts)
admin.site.register(ActivityLog)
admin.site.register(Company)
admin.site.register(CompanyBranch)
admin.site.register(Affordability)
admin.site.register(Payment)
admin.site.register(Mandate)
admin.site.register(Bank)
admin.site.register(BankBranch)
admin.site.register(Element)
admin.site.register(ElementCategory)
admin.site.register(ElementGroup)
admin.site.register(TesterTable)
