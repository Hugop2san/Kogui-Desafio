from .models import Usuario, Operacao
from .calculos import CalculoOperacoes #separacao de responsabilidade com operacao logica
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class OperacaoSerializer(serializers.ModelSerializer):
    usuario_id = serializers.IntegerField(read_only=True) 
    class Meta:
        model = Operacao
        fields = ['idoperacao', 'usuario_id', 'parametros', 'resultado']
    
    def validate_parametros(self, value):
        """Valida se os parâmetros estão no formato correto (ex: '1+2')"""
        if CalculoOperacoes.calcular_parametros(value) is None:
            raise serializers.ValidationError("Formato inválido, digite formato certo >>>>> 5+3 ")
        return value
    
    def create(self, validated_data):
        """Calcula o resultado automaticamente antes de salvar"""
        parametros = validated_data['parametros']
        validated_data['resultado'] = str(CalculoOperacoes.calcular_parametros(parametros))
        return super().create(validated_data)