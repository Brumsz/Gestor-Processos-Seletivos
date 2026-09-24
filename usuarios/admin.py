from django.contrib import admin

from usuarios.models import Usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id','primeiro_nome','ultimo_nome','email','data_inscricao')
    list_display_links = ('id','primeiro_nome')
    list_per_page = 20
    search_fields = ('id','primeiro_nome')

