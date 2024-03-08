# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"profs", views.ProfileViewSet, basename="profile")
router.register(r"locations", views.LocationViewSet)
router.register(r"hospital-profiles", views.HospitalProfileViewSet)
router.register(r"patient-profiles", views.PatientProfileViewSet)
router.register(r"hospital-services", views.HospitalServiceViewSet)
router.register(r"doctors", views.DoctorViewSet)
router.register(r"nurses", views.NurseViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
