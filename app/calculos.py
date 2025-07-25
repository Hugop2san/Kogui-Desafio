import re

class CalculoOperacoes:
    @staticmethod
    def calcular_parametros(parametros):
        try:
            
            if not re.match(r'^\d+[+\-*/]\d+$', parametros):
                return None
            
            # Extrai valores e operador da logica regex
            valor1, operador, valor2 = re.split('([+\\-*/])', parametros)
            valor1 = float(valor1)
            valor2 = float(valor2)
            
            # Calcula (substitua por switch-case se preferir)
            if operador == '+':
                return valor1 + valor2
            elif operador == '-':
                return valor1 - valor2
            elif operador == '*':
                return valor1 * valor2
            elif operador == '/':
                return valor1 / valor2 if valor2 != 0 else None
            else:
                return None
        except:
            return None