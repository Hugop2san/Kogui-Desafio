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


class RegistroUsuario(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class DetalheUsuario(generics.RetrieveAPIView):
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
        try:
            print("Dados brutos:", request.body)  # Debug adicional
            print("Dados parseados:", request.data) 
            
            # Verificação explícita dos dados
            if not request.data or 'parametros' not in request.data:
                return Response(
                    {"error": "O campo 'parametros' é obrigatório no formato {'parametros': '5+3'}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            parametros = str(request.data['parametros']).strip()
            resultado = CalculoOperacoes.calcular_parametros(parametros)
            
            if resultado is None:
                return Response(
                    {"error": "Parâmetros inválidos. Use formato 'número+operador+número' (Ex: 5+3)"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            operacao = Operacao.objects.create(
                usuario_id=usuario_id,
                parametros=parametros,
                resultado=resultado
            )
            
            return Response(OperacaoSerializer(operacao).data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {"error": f"Erro no servidor: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

