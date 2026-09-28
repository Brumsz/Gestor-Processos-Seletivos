from django.contrib import admin

from usuarios.models import Usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id','username','first_name', 'last_name', 'email')
    list_display_links = ('id','username')
    list_per_page = 20
    search_fields = ('id','username')

admin.site.register(Usuario,Usuarios)
