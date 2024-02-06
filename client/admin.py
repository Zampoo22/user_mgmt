from django.contrib import admin
from .models import Employee, EmployeeProfile

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    pass


