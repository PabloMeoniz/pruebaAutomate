
import pytest
import operaciones
#MODULARIZAR
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def dividir(a, b):
    if b==0:
        raise ValueError('error al dividir por cero')
    return a // b
def multiplicar(a, b):
    return a * b

def calculadora_simple(operacion, a, b):
    try:
        a = int(a)
        b = int(b)
        if operacion == 'sumar':
            return sumar(a, b)
        elif operacion == 'restar':
            return restar(a, b)
        elif operacion == 'dividir':
            return dividir(a, b)
        else:
            return KeyError('Operacion no valida')
    except ZeroDivisionError:
        return 'Error : no se puede dividir por cero'
    except ValueError:
        return 'Error : los valores deben ser numericos'
'''       
print(calculadora_simple("sumar", 1, 1)) # 2
print(calculadora_simple("restar", 1, 1)) # 0
print(calculadora_simple("dividir", 1, 1)) # 1
print(calculadora_simple("dividir", 1, 0)) # ERROR ZERODIVISIONERROR
print(calculadora_simple("dividir", 1, 'R')) # ERROR valueError
print(calculadora_simple("multiplicar", 1, 1)) # ERROR keyerror
'''