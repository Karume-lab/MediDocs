from rest_framework import permissions


class DoctorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True#request.user.is_authenticated and request.user.doctor


class NursePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True#request.user.is_authenticated and request.user.nurse
