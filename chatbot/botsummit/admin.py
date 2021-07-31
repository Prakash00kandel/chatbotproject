from django.contrib import admin
from .models import UserInfo


# Register your models here.

# admin.site.register(UserInfo)

@admin.register(UserInfo)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "desired_sub",)
    list_filter = ("desired_sub",)
    search_fields = ("name",)
    fields = ("name", "phone_number", "desired_sub", "notes")



