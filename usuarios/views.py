from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from usuarios.models import Usuario
from usuarios.serializer import UsuarioSerializer

class UsuarioViewsets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UsuarioSerializer
    
    def get_queryset(self):
        return Usuario.objects.filter(id=self.request.user.id)
    
    

class UsuarioCreateUserViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.none()
    
    def perform_create(self, serializer):
            user = serializer.save()
            password = self.request.data['password']
            user.set_password(password)
            user.save()

