from django.db import models

class Usuario(models.Model):
    usuario_id   = models.AutoField(primary_key=True) 
    nome_usuario        = models.CharField(max_length=300)
    email       = models.CharField(max_length=300)
    senha       = models.CharField(max_length=300)
    stlnclusao  = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_usuario



class Operacao(models.Model):
    idoperacao = models.AutoField(primary_key=True)  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='operacoes')
    parametros = models.CharField(max_length=20) 
    resultado = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.usuario} - {self.parametros} = {self.resultado}"
   