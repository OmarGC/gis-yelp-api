from django.contrib import admin

from .models import Business


# Register your models here.
@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    search_fields = ("business_id",)