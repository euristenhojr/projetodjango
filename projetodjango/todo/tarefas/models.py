from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = (
        ('B','BAIXA'),
        ('M', 'MÉDIA'),
        ('A', 'ALTA'),
    )

    nome = models.CharField(max_length=100, verbose_name='Nome')
    nome = models.TextField(verbose_name='Descrição', blank=True)
    data_final = models.DateField(verbose_name='Data Final')
    prioridade = models.CharField(verbose_name='Prioridade', max_length=1, choices=PRIORIDADE_CHOICES)
    categoria = models.ForeignKey(Categoria,verbose_name='Categoria')
