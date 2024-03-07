from django.urls import path
from .views import CustomUserListCreateView, CustomUserRetrieveUpdateDestroyView

urlpatterns = [
    path("", CustomUserListCreateView.as_view(), name="user-list-create"),
    path(
        "<int:pk>/",
        CustomUserRetrieveUpdateDestroyView.as_view(),
        name="user-retrieve-update-destroy",
    ),
]
