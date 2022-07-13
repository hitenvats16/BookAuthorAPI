from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['email', 'username']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'display_name', 'mobile_phone',)}),
    )
    fieldsets = (
        (None, {'fields': ('display_name', 'mobile_phone',
         'no_of_books_published', 'username', 'email')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
