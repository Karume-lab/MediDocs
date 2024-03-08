from django.contrib import admin
from . import models

admin.site.register(models.HospitalProfile)
admin.site.register(models.HospitalService)
admin.site.register(models.Location)
admin.site.register(models.PatientProfile)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital')
    list_filter = ('hospital',)
    search_fields = ('user__username', 'user__email')

admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Nurse)
