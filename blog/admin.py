from django.contrib import admin

from blog.models import BlogRecord


# Register your models here.

@admin.register(BlogRecord)
class BlogRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'created_at')