from django.contrib import admin
from .models import CategoryMaster, StatusMaster, Task
# Register your models here.

@admin.register(CategoryMaster)
class CategoryMasterAdmin(admin.ModelAdmin):
    pass

@admin.register(StatusMaster)
class StatusMasterAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category', 'status', 'created_at', 'updated_at']
