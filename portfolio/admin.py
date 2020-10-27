from django.contrib import admin
from portfolio.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology')
    search_fields = ['title', 'technology']
    fieldsets = [
            ('Project', {'fields': ['title', 'summary']}),
            ('Information', {'fields': ['description', 'technology']}),
            ('Media', {'fields': ['image']}),
            ('URL', {'fields': ['url']}),
            ]

admin.site.register(Project, ProjectAdmin)
