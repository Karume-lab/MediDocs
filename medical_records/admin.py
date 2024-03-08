from django.contrib import admin
from . import models


class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ("name", "hospital")
    list_filter = ("hospital",)
    search_fields = ("user__username", "user__email")


admin.site.register(models.MedicalRecord, MedicalRecordAdmin)
