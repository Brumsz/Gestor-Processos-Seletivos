from django.db import models

class Usuario(models.Model):
    primeiro_nome = models.CharField(max_length=100,blank=False)
    ultimo_nome = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False,unique=True)
    password = models.CharField(blank=False)
    data_inscricao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.primeiro_nome