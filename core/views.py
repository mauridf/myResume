from django.views.generic import TemplateView

from .models import DadosPessoais,Sumario, Experiencia, TipoSkill, Skill, Educacao, Lingua, Interesse

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['dadospessoais'] = DadosPessoais.objects.all
        context['sumario'] = Sumario.objects.all()
        context['experiencia'] = Experiencia.objects.all
        context['tiposkill'] = TipoSkill.objects.all
        context['skill'] = Skill.objects.order_by('tiposkill_id').all
        context['educacao'] = Educacao.objects.all
        context['lingua'] = Lingua.objects.all
        context['interesse'] = Interesse.objects.all
        return context
