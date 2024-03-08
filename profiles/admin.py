from django.contrib import admin
from . import models


class HospitalProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    list_filter = ("name",)


class PatientProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_of_birth",
        "location",
    )
    list_filter = ("user",)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "hospital")
    list_filter = ("hospital",)
    search_fields = ("user__username", "user__email")


class HospitalServiceAdmin(admin.ModelAdmin):
    list_display = ("category",)
    list_filter = ("category",)


class LocationAdmin(admin.ModelAdmin):
    list_display = ("address", "latitude", "longitude")
    list_filter = ("address",)


class NurseAdmin(admin.ModelAdmin):
    list_display = ("name", "hospital")
    list_filter = ("name",)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "hospital_profile", "patient_profile")
    list_filter = ("user",)


admin.site.register(models.Nurse, NurseAdmin)
admin.site.register(models.PatientProfile, PatientProfileAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.HospitalProfile, HospitalProfileAdmin)
admin.site.register(models.HospitalService, HospitalServiceAdmin)
