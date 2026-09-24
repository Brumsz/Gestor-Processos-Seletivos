from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    class Meta:
        model = Usuario
        fields = '__all__'