from rest_framework import viewsets

from vagas.models import Vaga
from vagas.serializer import VagaSerializer

class VagaViewsets(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
