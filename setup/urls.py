from rest_framework import routers
from django.contrib import admin
from django.urls import path,include

from vagas.views import VagaViewsets
from usuarios.views import UsuarioViewsets,UsuarioCreateUserViewset

router = routers.DefaultRouter()
router.register('vagas',VagaViewsets,basename='Vagas')
router.register('usuario',UsuarioViewsets,basename='Usuario')
router.register('criar',UsuarioCreateUserViewset,basename='Criar')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
