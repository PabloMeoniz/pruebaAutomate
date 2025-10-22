
#tipos de datos

#str => String => cadena de texto
#int => Enteros
#float => Decimales
#bool => True o False

nombre = "Luis"
edad = 39
altura = 1.60
esMayorDeEdad = True
#Entrada y salida de datos
#print(nombre)
#anioDeNacimiento = int(input("ingresa tu año de nacimiento: "))
#print(type(anioDeNacimiento))
#Convertir Tipos de Datos
resultado = 2 + 3
potencia = 2**2

division = 10 // 5
#print(division)
resto = 4 % 2
#print(resto)
result = 5 == 2
#(edad >= 18) and (licencia == True) => True
cursarEnOtra = True
not(edad > 18 or cursarEnOtra)

'''#puntuacion = int(input("ingrese una nota - (0-10)"))
if puntuacion >= 9:
    print("Exelente")
elif puntuacion >= 8:
    print("bien")
else:
    print('desaprobado') 
'''

#range(stop) 10
#range(start, stop) 2 - 11
#range(start, stop, step) 2 - 11 -- 2
'''
for i in range(12):
    if i==5:
        continue
    print(i)
'''
'''
i=1
while i <= 5:
    print(i)
    i = i + 1
'''
#listas
'''
mi_lista = ['Argentina', 200, True]
            #0,1,2
for i in mi_lista:
    print(i)
    

mi_lista.append(5000)
mi_lista.insert(1, "Paises Bajos")
'''
#for i in mi_lista: #imprime todos los elementos de la lista
#    print(i)
#print(mi_lista)

#tuplas
mi_tupla = ("Celeste", 200, "Rojo")
#INMUTABLE
#mi_tupla[1] = 400
#print(mi_tupla[1])
#diccionarios dicc
data = {
    #"clave":valor,
}
'''
persona = {
    "nombre" : "Jaime",
    "apellido" : "Desconocido",
    "edad" : 34
}
'''
'''
print(persona.keys())
print(persona.values())
print(persona.items())
'''

#Funciones
'''
def saludo(nombre):
    print(f"Hola {nombre}")
saludo("Nati")
saludo("Raul")
'''
'''
def saludo(nombre):
    return f'Hola {nombre}'
saludo("Nati")
saludo("Raul")
print(saludo('Nati'))
'''


'''
#MODULARIZAR
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def dividir(a, b):
    return a // b
def multiplicar(a, b):
    return a * b

def calculadora_simple(operacion, a, b):
    if operacion == 'sumar':
        return sumar(a, b)
    elif operacion == 'restar':
        return restar(a, b)
    elif dividir == 'dividir':
        return dividir(a, b)
    elif operacion == 'multiplicar':
        return multiplicar(a, b)
    else:
        return 'Operacion No Valida'
print(calculadora_simple("sumar", 7, 3))
'''
'''
try:
    resultado= 10/0
except ZeroDivisionError as e:
    print(f'Error : No se puede dividir entre 0')
    print(f'Error : {e}')
'''
'''
try:
    numero = int('abc')
except ValueError as e:
    print(f'Error : {e}')
'''

'''
persona = {
    "nombre" : "Jaime",
    "apellido" : "Desconocido",
    "edad" : 34
}
try:
    print(persona['documento'])
except KeyError as e:
    print('la clave no existe')
'''

#MODULARIZAR
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def dividir(a, b):
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
usuarios = {
    "ana":{"edad":56},
    "jose":{"edad":77}
}
def pedirNombre():
    try:
        nombre = input('Ingrese el nombre ') #japon
        edad = usuarios[nombre]["edad"]
        print(f'{nombre} tiene {edad} años')
    except KeyError:
        print(f'ERROR : no se encontro edad de ese nombre ')
#pedirNombre()
'''
try:
    edad = int(input('ingresa tu edad '))
    print(f'El año que viene tendras {edad + 1} años ')
except ValueError:
    print('debes poner solo numeros')
'''