from django.contrib import admin
from .models import BugReport, FeatureRequest

# admin.site.register(BugReport)
# admin.site.register(FeatureRequest)

@admin.action(description='Change status on "In proccess"')
def change_status_in_proccess(modeladmin, request, queryset):
    queryset.update(status="In proccess")

@admin.action(description='Change status on "Completed"')
def change_status_completed(modeladmin, request, queryset):
    queryset.update(status="Completed")

@admin.action(description='Change status on "Accepted"')
def change_status_accepted(modeladmin, request, queryset):
    queryset.update(status="Accepted")

@admin.action(description='Change status on "Rejected"')
def change_status_rejected(modeladmin, request, queryset):
    queryset.update(status="Rejected")

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title','description','project','task','status','priority', 'created_at','update_at')
    list_filter = ('status', 'task','project')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title','description','project','task','priority')
        }),
    )
    list_editable = ('status', 'priority')
    actions = [change_status_in_proccess, change_status_completed]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title','description','project','task','status','priority', 'created_at','update_at')
    list_filter = ('status', 'task','project')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title','description','project','task','priority')
        }),
    )
    list_editable = ('status', 'priority')
    actions = [change_status_accepted, change_status_rejected]

    

# Register your models here.
