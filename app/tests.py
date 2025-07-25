from django.test import TestCase


#   SETAR USUARIO
# curl -X POST http://localhost:8000/api/registro/ -H "Content-Type: application/json" -d "{\"nome_usuario\": \"Douglas Pinto\", \"email\": \"douglas@egmail.com\", \"senha\": \"123\"}"

#   SETAR CALCULO MATEMATICO COM ID DO USUARIO
# curl -X POST http://localhost:8000/api/usuarios/11/operacoes/ -H "Content-Type: application/json" -d "{\"parametros\": \"10+90\"}"
