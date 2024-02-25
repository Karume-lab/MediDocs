from django.urls import path, include
from doctors.routers import router


urlpatterns = [
    path("api/", include(router.urls)),
]
