from django.db import models

class Usuario(models.Model):
    IDusuario   = models.AutoField(primary_key=True) 
    nome        = models.CharField(max_length=300)
    Email       = models.CharField(max_length=300)
    Senha       = models.CharField(max_length=300)
    Stlnclusao  = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome



class Operacao(models.Model):
    IDOperacao      = models.IntegerField(primary_key=True)
    IDUsiario       = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    Parametros      = models.CharField(max_length=2)
    Resultado       = models.CharField(max_length=1000)
    Stlnclusao      = models.BooleanField(default=True)
    
    def __str__(self):
        return f" {self.IDUsiario.nome} - {self.Parametros} - {self.Resultado}"


