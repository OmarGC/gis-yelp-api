from django.contrib import admin

from .models import YelpUser


# Register your models here.
@admin.register(YelpUser)
class YelpUserAdmin(admin.ModelAdmin):
    search_fields = ("user_id",)