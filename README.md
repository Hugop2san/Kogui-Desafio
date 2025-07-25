# 🧮 Projeto Django REST - Cadastro de Usuário e Calculadora com Histórico

Este projeto é um **MVP em Django REST Framework (DRF)** usando **SQLite** como banco de dados.  
Ele permite:
- Cadastrar usuários.
- Realizar operações matemáticas.
- Manter um **histórico de operações** vinculado a cada usuário.

---

## 🚀 Funcionalidades
1. **Cadastro de usuários** (endpoint `api/registro/`).
2. **Registro de operações matemáticas** (endpoint `api/usuarios/<id>/operacoes/`).
3. **Histórico de operações** por usuário.
4. **Persistência em SQLite** com `Usuario` e `Operacao`.
5. **Soft Delete** (`ativo = True/False`) para manter registros lógicos.

---

## 🔧 Como Rodar
### 1. Subir o servidor Django
```bash
python manage.py runserver
```

## 🧑‍💻 Como Usar a API via CMD

### **1. Registrar um Usuário**
Envia um `POST` para o endpoint `/api/registro/` com os dados do usuário:
```bash
curl -X POST http://localhost:8000/api/registro/ \
-H "Content-Type: application/json" \
-d '{"nome_usuario": "Douglas Pinto", "email": "douglas@egmail.com", "senha": "123"}'
```

### **2. Realizar uma Operação Matemática**
Envia um `POST` para o endpoint `/api/usuarios/<id>/operacoes/` passando a expressão matemática:
```bash
curl -X POST http://localhost:8000/api/usuarios/11/operacoes/ \
-H "Content-Type: application/json" \
-d '{"parametros": "10+90"}'
```

### **3. Listar Histórico de Operações**
Envia um `GET` para o endpoint `/api/usuarios/<id>/operacoes/` para consultar todas as operações do usuário:
```bash
curl -X GET http://localhost:8000/api/usuarios/11/operacoes/
```















