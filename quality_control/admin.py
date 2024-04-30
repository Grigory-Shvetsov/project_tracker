from django.contrib import admin
from .models import BugReport, FeatureRequest

# admin.site.register(BugReport)
# admin.site.register(FeatureRequest)


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title','description','project','task','status','priority', 'created_at','update_at')
    list_filter = ('status', 'task','project')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project')
        }),
    )


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title','description','project','task','status','priority', 'created_at','update_at')
    list_filter = ('status', 'task','project')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project')
        }),
    )
    



# Register your models here.
