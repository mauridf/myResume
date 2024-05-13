from django.contrib import admin

from .models import DadosPessoais,Sumario, Experiencia, TipoSkill, Skill, Educacao, Lingua, Interesse

@admin.register(DadosPessoais)
class DadosPessoaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'ativo', 'modificado')

@admin.register(Sumario)
class SumarioAdmin(admin.ModelAdmin):
    list_display = ('sumario', 'ativo', 'modificado')

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'ativo', 'modificado')

@admin.register(TipoSkill)
class TipoSkillAdmin(admin.ModelAdmin):
    list_display = ('tiposkill','ativo','modificado')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('tiposkill','nome','ativo','modificado')

@admin.register(Educacao)
class EducacaoAdmin(admin.ModelAdmin):
    list_display = ('instituicao', 'curso', 'ativo', 'modificado')

@admin.register(Lingua)
class LinguaAdmin(admin.ModelAdmin):
    list_display = ('lingua', 'nivel', 'ativo', 'modificado')

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('interesse','ativo','modificado')

