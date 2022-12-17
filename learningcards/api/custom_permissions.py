from rest_framework.permissions import BasePermission, SAFE_METHODS

class GuestsReadOnly(BasePermission):
    """
    Read-only mode for guests.
    """

    message = 'El Modo Invitados esta habilitado para solo lectura.'

    def has_permission(self, request, view):
        
        if request.user.username == "Invitados":
            return request.method in SAFE_METHODS
        
        return True