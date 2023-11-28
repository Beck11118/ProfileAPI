from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to create, edit, delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if hasattr(obj, 'owner'):  # Check if the model has an 'owner' field
            return obj.owner == request.user
        elif hasattr(obj, 'profile_item'):  # Check if the model has a 'profile_item' field
            return obj.profile_item.owner == request.user
        
        return False