from django.contrib import admin
from . import models


class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    list_filter = ("name",)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "hospital")
    list_filter = ("hospital",)
    search_fields = ("user__username", "user__email")


class HospitalServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("name",)


class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "latitude", "longitude")
    list_filter = ("name",)


class NurseAdmin(admin.ModelAdmin):
    list_display = ("name", "hospital")
    list_filter = ("name",)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "hospital_profile", "patient_profile")
    list_filter = ("user",)


admin.site.register(models.PatientProfile)
admin.site.register(models.Nurse, NurseAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.HospitalProfile, HospitalAdmin)
admin.site.register(models.HospitalService, HospitalServiceAdmin)
