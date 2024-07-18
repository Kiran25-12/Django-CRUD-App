from django.contrib import admin
from .models import EmployeeData
# Register your models here.
admin.site.register(EmployeeData)

# @admin.register(EmployeeData)
# class employeedata1(admin.ModelAdmin):
#     list_display = ['id','name']