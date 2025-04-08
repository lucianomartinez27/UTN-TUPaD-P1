import math

def imprimir_hola_mundo():
    saludar_usuario("Mundo")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def segundos_a_horas(cantidad_segundos):
    return cantidad_segundos // 60 // 60

def tabla_multiplicar(numero):
    tabla = ""
    for i in range(1, 11):
        tabla += f"{i} * {numero} = {i * numero}\n"
    return tabla

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

def calcular_imc(peso_en_kg, altura_en_metros):
    return peso_en_kg / (altura_en_metros ** 2)

def celsius_a_fahrenheit(grados_celsius):
    return (grados_celsius * (9/5)) + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3