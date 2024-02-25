from rest_framework import permissions


class IsDoctorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user making the request is the doctor assigned to the medical record
        return obj.doctor == request.user
