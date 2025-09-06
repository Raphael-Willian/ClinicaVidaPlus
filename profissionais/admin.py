from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profissional
from .forms import ProfissionalChangeForm, ProfissionalCreationForm


class ProfissionalAdmin(UserAdmin):
    add_form = ProfissionalCreationForm
    form = ProfissionalChangeForm
    model = Profissional
    list_display = ["username", "is_staff", "is_active"]
    list_filter = ["is_staff", "is_active"]

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informações pessoais', {'fields': (
            'nome_completo', 'especialidade', 'telefone', 'nascimento',
            'cpf', 'genero', 'endereco', 'cep', 'registro_profissional', 'status', 'comissao'
        )}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'nome_completo', 'especialidade', 'telefone', 'nascimento',
                'cpf', 'genero', 'endereco', 'cep', 'registro_profissional', 'status', 'comissao',
                'is_staff', 'is_active'
            ),
        }),
    )

    search_fields = ('email', 'nome_completo', 'cpf')
    ordering = ('email',)


admin.site.register(Profissional, ProfissionalAdmin)
