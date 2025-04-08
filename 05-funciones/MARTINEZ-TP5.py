# Práctico N5 - Funciones
# Alumno: Martinez Luciano Joaquin

from funciones import (imprimir_hola_mundo,
                       saludar_usuario,
                       informacion_personal,
                       calcular_area_circulo,
                       calcular_perimetro_circulo,
                       segundos_a_horas,
                       tabla_multiplicar,
                       operaciones_basicas,
                       calcular_imc,
                       celsius_a_fahrenheit,
                       calcular_promedio)


def actividad_1():
    # 1. Crear una función llamada imprimir_hola_mundo que imprima por
    # pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
    # programa principal.
    imprimir_hola_mundo()

def actividad_2():
    # 2. Crear una función llamada saludar_usuario(nombre) que reciba
    # como parámetro un nombre y devuelva un saludo personalizado.
    # Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
    # principal solicitando el nombre al usuario.
    nombre = input("Ingresa tu nombre: ")
    saludar_usuario(nombre)

def actividad_3():
    # 3. Crear una función llamada informacion_personal(nombre, apellido,
    # edad, residencia) que reciba cuatro parámetros e imprima: “Soy
    # [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

def actividad_4():
    # 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
    # y devuelva el área del círculo.
    # calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
    # Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
    radio = float(input("Ingrese el radio del circulo: "))
    print(f"El area del circulo es {calcular_area_circulo(radio)} mientras que su perimetro es {calcular_perimetro_circulo(radio)}")

def actividad_5():
    # 5. Crear una función llamada segundos_a_horas(segundos) que reciba
    # una cantidad de segundos como parámetro y devuelva la cantidad
    # de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
    segundos = int(input("Ingrese la cantidad de segundos para pasar a horas: "))
    print(f"{segundos} segundo son {segundos_a_horas(segundos)} horas")

def actividad_6():
    # 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
    # número como parámetro y imprima la tabla de multiplicar de ese
    # número del 1 al 10. Pedir al usuario el número y llamar a la función.
    numero = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
    print(f"{tabla_multiplicar(numero)}")

def actividad_7():
    # 7. Crear una función llamada operaciones_basicas(a, b) que reciba
    # dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
    # Mostrar los resultados de forma clara
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    print(f"Resultado de sumar, restar, multipliar y dividir los números {a} y {b}")
    print(f"{operaciones_basicas(a, b)}")

def actividad_8():
    # 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
    # peso en kilogramos y la altura en metros, y devuelva el índice de
    # masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
    peso_en_kg = float(input("Ingrese su peso en kg: "))
    altura_en_metros = float(input("Ingrese su altura en metros: "))
    print(f"Su IMC es {calcular_imc(peso_en_kg, altura_en_metros)}")

def actividad_9():
    # 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
    # una temperatura en grados Celsius y devuelva su equivalente en
    # Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
    # resultado usando la función.
    temperatura_en_celsius = float(input("Ingrese la temperatura en celsius: "))
    print(f"{temperatura_en_celsius} grados celsius son {celsius_a_fahrenheit(temperatura_en_celsius)} grados fahrenheit")

def actividad_10():
    # 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
    # tres números como parámetros y devuelva el promedio de ellos.
    # Solicitar los números al usuario y mostrar el resultado usando esta
    # función.
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    print(f"El primedio de {a} + {b} + {c} es {calcular_promedio(a, b, c)}")

if __name__ == '__main__':
    def elegir_actividad():
        numero = input("Elija qué actividad quiere ejecutar: 1-10: o cualquier otro número para salir: ")
        actividades = {
            '1': actividad_1,
            '2': actividad_2,
            '3': actividad_3,
            '4': actividad_4,
            '5': actividad_5,
            '6': actividad_6,
            '7': actividad_7,
            '8': actividad_8,
            '9': actividad_9,
            '10': actividad_10
        }
        if  numero in actividades:
            return actividades[numero]
        else:
            return None
    actividad = elegir_actividad()
    while actividad is not None:
        actividad()
        actividad = elegir_actividad()
    print("Saló de la aplicación")



