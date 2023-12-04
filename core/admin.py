from django.contrib import admin

from .models import DadosPessoais,Sumario, Experiencia, TipoSkill, Skill, Educacao, Lingua, Interesse

@admin.register(DadosPessoais)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'ativo', 'modificado')

@admin.register(Sumario)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('sumario', 'ativo', 'modificado')

@admin.register(Experiencia)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'ativo', 'modificado')

@admin.register(TipoSkill)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('tiposkill','ativo','modificado')

@admin.register(Skill)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('tiposkill','nome','ativo','modificado')

@admin.register(Educacao)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('instituicao', 'curso', 'ativo', 'modificado')

@admin.register(Lingua)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('lingua', 'nivel', 'ativo', 'modificado')

@admin.register(Interesse)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('interesse','ativo','modificado')

