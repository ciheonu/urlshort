from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ['link', 'uuid', 'date_created']
    ordering = ['date_created']
    list_per_page = 20
