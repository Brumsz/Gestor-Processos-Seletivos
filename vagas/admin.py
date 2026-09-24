from django.contrib import admin

from vagas.models import Vaga

class Vagas(admin.ModelAdmin):
    list_display = ('id','nome','empresa','status','descricao','data_iscricao')
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome', 'empresa')

admin.site.register(Vaga,Vagas)

