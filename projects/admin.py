from django.contrib import admin
from .models import Project, Framework

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('project_name','user')

admin.site.register(Framework)
