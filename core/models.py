import uuid

from django.db import models

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criado = models.DateField('Criação',auto_now_add=True)
    modificado = models.DateField('Atualização',auto_now=True)
    ativo = models.BooleanField('Ativo?',default=True)

    class Meta:
        abstract = True

class DadosPessoais(Base):
    nome = models.CharField('Nome', max_length=100)
    profissao = models.CharField('Profissão', max_length=100)
    email = models.CharField('E-Mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)
    imagem = StdImageField('Imagem',upload_to=get_file_path,variations={'thumbs':{'width':400,'height':400, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    linkeddin = models.CharField('LinkedIn', max_length=100, default='#')
    github = models.CharField('GitHub',max_length=100,default='#')
    codepen = models.CharField('Codepen', max_length=100, default='#')

    class Meta:
        verbose_name = 'DadoPessoal'
        verbose_name_plural = 'DadosPessoais'

    def __str__(self):
        return self.nome

class Sumario(Base):
    sumario = models.TextField('Bio', max_length=1000)

    class Meta:
        verbose_name = 'Sumario'
        verbose_name_plural = 'Sumarios'

    def __str__(self):
        return self.sumario


class Experiencia(Base):
    cargo = models.CharField('Cargo', max_length=100)
    empresa = models.CharField('Empresa', max_length=100)
    anoinicio = models.CharField('Ano de Início', max_length=4)
    anotermino = models.CharField('Ano de Término', max_length=4)
    resumo = models.TextField('Resumo de Atividades', max_length=500)
    tecnologia1 = models.CharField('Tecnologia Utilizada 01', max_length=100)
    tecnologia2 = models.CharField('Tecnologia Utilizada 02', max_length=100)
    tecnologia3 = models.CharField('Tecnologia Utilizada 03', max_length=100)
    tecnologia4 = models.CharField('Tecnologia Utilizada 04', max_length=100)
    tecnologia5 = models.CharField('Tecnologia Utilizada 05', max_length=100)
    tecnologia6 = models.CharField('Tecnologia Utilizada 06', max_length=100)
    tecnologia7 = models.CharField('Tecnologia Utilizada 07', max_length=100)
    tecnologia8 = models.CharField('Tecnologia Utilizada 08', max_length=100)

    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'

    def __str__(self):
        return self.cargo

class TipoSkill(Base):
    tiposkill = models.CharField('Tipo de Skill', max_length=100)

    class Meta:
        verbose_name = 'TipoSkill'
        verbose_name_plural = 'TiposSkill'

    def __str__(self):
        return self.tiposkill

class Skill(Base):
    tiposkill = models.ForeignKey('core.TipoSkill', verbose_name='TipoSkill', on_delete=models.CASCADE)
    nome = models.CharField('Nome da Skill', max_length=100)
    porcentagem = models.CharField('Porcentagem', max_length=3)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.nome

class Educacao(Base):
    instituicao = models.CharField('Instituição', max_length=100)
    curso = models.CharField('Curso', max_length=200)
    anoinicio = models.CharField('Ano de Início',max_length=4)
    anotermino = models.CharField('Ano de Termino', max_length=4)

    class Meta:
        verbose_name = 'Educacao'
        verbose_name_plural = 'Educações'

    def __str__(self):
        return self.instituicao

class Lingua(Base):
    NIVEL_CHOICES = (
        ('nativo', 'Nativo'),
        ('basico', 'Básico'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
    )
    lingua = models.CharField('Língua', max_length=100)
    nivel = models.CharField('Nível',max_length=15,choices=NIVEL_CHOICES)

    class Meta:
        verbose_name = 'Lingua'
        verbose_name_plural = 'Linguas'

    def __str__(self):
        return self.lingua

class Interesse(Base):
    interesse = models.CharField('Interesse',max_length=100)

    class Meta:
        verbose_name = 'Interesse'
        verbose_name_plural = 'Interesses'

    def __str__(self):
        return self.interesse