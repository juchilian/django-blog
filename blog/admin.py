from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .adminResources import BlogPostResource
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(ImportExportModelAdmin):
    resource_class = BlogPostResource