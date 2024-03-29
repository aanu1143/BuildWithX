# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', ]
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('bio','image')}),
        ('other', {'fields': ('username','first_name', 'last_name')})
    )


admin.site.register(CustomUser, CustomUserAdmin)
