from django.contrib import admin
from .models import Department, User, Request

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'department']
    search_fields = ['username']

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['request_number', 'request_type', 'amount', 'status', 'submission_date']
    list_filter = ['status', 'request_type']
    search_fields = ['request_number']
