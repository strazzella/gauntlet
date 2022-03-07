from django.contrib import admin

# Register your models here.
from .models import Document


class DocModelAdmin(admin.ModelAdmin):
    list_display = ["title", "last_accessed", "last_updated", "created"]

    class Meta:
        model = Document


admin.site.register(Document, DocModelAdmin)
