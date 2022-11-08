from django.contrib import admin
from .models import Task


class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created_at", "is_published")
    list_display_links = ("text", "id")
    search_fields = ("text",)
    list_editable = ("is_published",)
    list_filter = ("is_published",)


admin.site.register(Task, ToDoAdmin)

