from django.shortcuts import render, redirect , get_object_or_404
from .models import Usuario, Operacao
from .serializers import UsuarioSerializer, OperacaoSerializer
from .calculos import CalculoOperacoes

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from rest_framework.decorators import api_view
from rest_framework import status
import json



class RegistroUsuario(generics.CreateAPIView): # Natureza POST
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class DetalheUsuario(generics.RetrieveAPIView): # Natureza GET 
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class DashboardOperacao(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = [AllowAny]

    def get(self, request, usuario_id):
        operacoes = Operacao.objects.filter(usuario_id=usuario_id)
        serializer = OperacaoSerializer(operacoes, many=True)
        return Response(serializer.data)

    def post(self, request, usuario_id):
        usuario = get_object_or_404(Usuario, usuario_id=usuario_id)
        print("Dados recebidos:", request.data)  # Para depuração

        serializer = OperacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=usuario)  # Salva com o usuário associado
            return Response(
                {"id": serializer.instance.idoperacao, "resultado": serializer.instance.resultado},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)