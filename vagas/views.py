from rest_framework import viewsets

from vagas.models import Vaga
from vagas.serializer import ExibicaoVagaSerializer

class VagaViewsets(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Vaga.objects.filter(usuario=self.request.user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    serializer_class = ExibicaoVagaSerializer
