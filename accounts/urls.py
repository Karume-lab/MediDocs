# accounts/urls.py
from django.urls import path, include
from accounts.router import router

urlpatterns = [
    path("api/", include(router.urls)),
]
