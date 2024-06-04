"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['enrollment', 'name']
    # This tuple defines the layout and grouping of fields in the user detail view (when editing or creating a user). Each tuple inside fieldsets represents 
    # a section in   the form, with the first element being the section's label (or None for no label), and the second element being a dictionary containing the fields for that section.
    fieldsets = (
        (None, {'fields': ('enrollment', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        ( _('Permissions'),
                {
                    'fields': (
                        'is_active',
                        'is_staff',
                        'is_superuser',
                    )
                }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    """
        The first section has no label and contains the email and password fields.
        The second section is labeled "Personal Info" and contains the name field.
        The third section is labeled "Permissions" and contains the is_active, is_staff, and is_superuser fields.
    """
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'enrollment',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


admin.site.register(models.Student, UserAdmin)
admin.site.register(models.Assignement)