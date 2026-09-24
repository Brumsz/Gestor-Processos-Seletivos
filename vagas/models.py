from django.db import models
from django.conf import settings


class Vaga(models.Model):
    STATUS = (
        ('A','Andamento'),
        ('N','Negado'),
        ('AP','Aprovado'),
    )
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='vagas')
    nome = models.CharField(max_length=100,blank=False)
    empresa = models.CharField(max_length=30,blank=False)
    status = models.CharField(max_length=2,choices=STATUS,default='A')
    descricao = models.TextField(blank=False)
    data_inscricao = models.DateField()
    data_prazo = models.DateField()

    def __str__(self):
        return self.nome
