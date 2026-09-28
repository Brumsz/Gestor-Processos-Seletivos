from rest_framework import serializers

from vagas.models import Vaga

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        exclude = ['usuario']

class ExibicaoVagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        exclude = ['descricao','data_inscricao', 'data_prazo']

