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
    #renderer_classes = [JSONRenderer] # reavaliar         !!!
    permission_classes = [AllowAny]

    def get(self, request, usuario_id):
        operacoes = Operacao.objects.filter(usuario_id=usuario_id)
        serializer = OperacaoSerializer(operacoes, many=True)
        return Response(serializer.data)

    def post(self, request, usuario_id):
        usuario = get_object_or_404(Usuario, usuario_id=usuario_id)
        parametros = request.data.get('parametros', '')

        resultado = CalculoOperacoes.calcular_parametros(parametros)
        if resultado is None:
            return Response({"error": "Expressão inválida ou divisão por zero."}, status=status.HTTP_400_BAD_REQUEST)

        operacao = Operacao.objects.create(usuario=usuario, parametros=parametros, resultado=resultado)

        return Response(
            {"id": operacao.idoperacao, "resultado": operacao.resultado},
            status=status.HTTP_201_CREATED
        )
    
    
# VIEW que alimente meu frontend
class LoginOuCadastroUsuario(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        nome = request.data.get('nome_usuario')
        email = request.data.get('email')
        senha = request.data.get('senha')

        if not nome or not email or not senha:
            return Response({"error": "Preencha todos os campos."}, status=status.HTTP_400_BAD_REQUEST)

        email = email.lower()
        senha = senha.lower()
        nome = nome.lower()

        usuario, criado = Usuario.objects.get_or_create(
            email=email,
            defaults={'nome_usuario': nome, 'senha': senha}
        )

        # Se já existe, validar a senha
        if not criado and usuario.senha != senha:
            return Response({"error": "Senha incorreta."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UsuarioSerializer(usuario)
        return Response({
            "mensagem": "Usuário criado com sucesso!" if criado else "Login bem-sucedido.",
            "usuario": serializer.data
        }, status=status.HTTP_200_OK)