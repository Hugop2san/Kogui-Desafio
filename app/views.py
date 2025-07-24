from django.shortcuts import render, redirect , get_object_or_404
from .models import Usuario, Operacao
from .views import registroUsuario, dashboardOperacao
from .serializers import UsuarioSerializer, OperacaoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .calculos import CalculoOperacoes

#rom .forms import UsuarioForm,  LoginForm, ProdutoForm
#from django.db.models import Count
#from django.contrib import messages



# COMEÇAR LOGICA DE VIEWS E CONF. URLS
class RegistroUsuario(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class DashboardOperacao(APIView):
    
    def get(self, request, usuario_id):
        operacoes = Operacao.objects.filter(usuario_id=usuario_id)
        serializer = OperacaoSerializer(operacoes, many=True)
        return Response(serializer.data)

    def post(self, request, usuario_id):
        parametros = request.data.get("parametros")
        
        # Usando o serviço de cálculo da class calculos.py
        resultado = CalculoOperacoes.calcular_parametros(parametros)
        if resultado is None:
            return Response({"error": "Parâmetros inválidos"}, status=400)
        
        operacao = Operacao.objects.create(
            usuario_id=usuario_id,
            parametros=parametros,
            resultado=resultado
        )
        serializer = OperacaoSerializer(operacao)
        return Response(serializer.data)
    
