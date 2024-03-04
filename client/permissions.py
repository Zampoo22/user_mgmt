from rest_framework import permissions

class EmployeeManagerPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return (request.user.employee_type == 'Manager' 
                or request.method == 'GET')