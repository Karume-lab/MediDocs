from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", views.CustomUserListView.as_view(), name="user-list"),
    path("register/", views.CustomUserCreateView.as_view(), name="user-register"),
    path("login/", views.CustomUserLoginView.as_view(), name="user-login"),
]
