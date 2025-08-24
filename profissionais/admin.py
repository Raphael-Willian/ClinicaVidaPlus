from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profissional


class ProfissionalAdmin(UserAdmin):
    model = Profissional
    list_display = ["email", "nome_completo", "is_staff", "is_active"]
    list_filter = ["is_staff", "is_active"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações pessoais", {"fields": ("nome_completo", "telefone", "especialidade")}),
        ("Permissões", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "nome_completo", "password1", "password2", "is_staff", "is_active")
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Profissional, ProfissionalAdmin)
