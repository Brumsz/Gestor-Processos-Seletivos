from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from vagas.models import Vaga

class VagaSerializer(serializers.ModelSerializer):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    class Meta:
        model = Vaga
        fields = '__all__'

