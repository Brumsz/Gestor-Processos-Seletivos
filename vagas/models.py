from django.db import models

from usuarios.models import Usuario

class Vaga(models.Model):
    STATUS = (
        ('A','Andamento'),
        ('N','Negado'),
        ('AP','Aprovado'),
    )
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='vagas')
    nome = models.CharField(max_length=100,blank=False)
    empresa = models.CharField(max_length=30,blank=False)
    status = models.CharField(max_length=2,choices=STATUS,default='A')
    descricao = models.TextField(blank=False)
    data_iscricao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
