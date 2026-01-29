from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm   # user create form
    form = CustomUserChangeForm         # user update form     
    model = CustomUser
    list_display = ["email", "username", "age", "is_staff",]

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
