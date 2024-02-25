from rest_framework.routers import DefaultRouter
from .viewsets import RegistrationView, LoginView, LogoutView, ChangePasswordView

router = DefaultRouter()

# Register the views with the router
router.register(r'registration', RegistrationView, basename='registration')
router.register(r'login', LoginView, basename='login')
router.register(r'logout', LogoutView, basename='logout')
router.register(r'change-password', ChangePasswordView, basename='change-password')
