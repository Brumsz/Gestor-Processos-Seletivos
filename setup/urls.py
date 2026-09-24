from rest_framework import routers
from django.contrib import admin
from django.urls import path,include

from vagas.views import VagaViewsets
from usuarios.views import UsuarioViewsets

router = routers.DefaultRouter()
router.register('vagas',VagaViewsets,basename='Vagas')
router.register('usuarios',UsuarioViewsets,basename='Usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
