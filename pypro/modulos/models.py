from django.db import models
from ordered_model.models import OrderedModel
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField(null=True)
    descricao = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(_("order"), editable=False, db_index=True, null=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalhe', kwargs={'slug': self.slug})


class Aula(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    modulo = models.ForeignKey('Modulo', on_delete=models.PROTECT)
    order_with_respect_to = 'modulo'

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:aula', kwargs={'slug': self.slug})
