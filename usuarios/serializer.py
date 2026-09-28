from rest_framework import serializers

from usuarios.models import Usuario
from vagas.serializer import ExibicaoVagaSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    vagas = ExibicaoVagaSerializer(many=True,read_only=True)

    class Meta:
        model = Usuario
        fields = ['id','username','email','password', 'vagas']