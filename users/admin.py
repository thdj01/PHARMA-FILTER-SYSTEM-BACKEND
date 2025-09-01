# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Unregister the default UserAdmin if it's already registered
# This can happen in some Django versions, but it's good practice to be safe
# from django.contrib.auth.models import User as AuthUser
# if admin.site.is_registered(AuthUser):
#     admin.site.unregister(AuthUser)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Add custom fields to the list display and fieldsets
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'groups')
    
    # Add 'role' and 'employee_id' to the fieldsets for the user detail/edit page
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'employee_id')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('role', 'employee_id', 'first_name', 'last_name')}),
    )