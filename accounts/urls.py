from django.urls import path
from .views import CustomUserCreateView, CustomUserLoginView, CustomUserListView

urlpatterns = [
    path("", CustomUserListView.as_view(), name="user-list"),
    path("register/", CustomUserCreateView.as_view(), name="user-register"),
    path("login/", CustomUserLoginView.as_view(), name="user-login"),
]
