# Práctico N4 - Estructuras Condicionales
# Alumno: Martinez Luciano Joaquin
import random
import statistics


def actividad_1():
    # 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
    # (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
    for i in range(0, 101):
        print(i)

def actividad_2():
    # 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
    # dígitos que contiene.
    numero_original = int(input("Ingrese un número entero: "))
    numero = abs(numero_original)
    digitos = 1  # comenzamos en 1 para tener en cuenta el número 0
    while numero >= 10:
        numero = numero // 10
        digitos += 1
    print(f"El número {numero_original} tiene {digitos} digito/s")

def actividad_3():
    # 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
    # dados por el usuario, excluyendo esos dos valores.
    inicio_rango = int(input("Ingrese el inicio del rango: "))
    final_rango = int(input("Ingrese el final del rango: "))
    total = 0
    for i in range(inicio_rango+1, final_rango):
        total += i
    print(f"La suma de los números entre {inicio_rango} y {final_rango} (excluyéndolos) es igual a {total}")

def actividad_4():
    # 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
    # secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
    # un 0
    numero_ingresado = None
    total = 0
    while numero_ingresado != 0:
        numero_ingresado = int(input(
            f"Ingrese el número que quiere sumar, el total hasta ahora es {total}. Ingrese 0 para salir: "))
        total += numero_ingresado

def actividad_5():
    # 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
    # programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

    numero_aleatorio = random.randint(0, 9)
    total_intentos = 1
    numero_ingresado = int(input("Adivine el número entre 0 y 9. Tiene intentos ilimitados: "))
    while numero_aleatorio != numero_ingresado:
        numero_ingresado = int(input("Incorrecto. Intente otra vez: "))
        total_intentos += 1
    print(f"Adivinó! Le tomó {total_intentos} intentos encontrar el número")

def actividad_6():
    # 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
    # entre 0 y 100, en orden decreciente.
   for numero_par in range(100, 1, -2):
       print(numero_par)

def actividad_7():
    # 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
    # número entero positivo indicado por el usuario
    inicio_rango = 0
    final_rango = int(input("Ingrese el final del rango: "))
    total = 0
    for i in range(inicio_rango, final_rango+1):
        total += i
    print(f"La suma de los números entre {inicio_rango} y {final_rango} (incluyéndolos) es igual a {total}")


def actividad_8():
    # 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
    # programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
    # negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
    # menor, pero debe estar preparado para procesar 100 números con un solo cambio).

    cantidad_pares = 0
    cantidad_impares = 0
    cantidad_positivos = 0
    cantidad_negativos = 0
    for i in range(100):
        numero_ingresado = int(input("Ingrese un número entero entero: "))
        if numero_ingresado > 0:
            cantidad_positivos += 1
        elif numero_ingresado < 0:
            cantidad_negativos += 1
        if (numero_ingresado % 2) == 0:
            cantidad_pares += 1
        else:
            cantidad_impares +=1
    print(f"""Ingresaste:
            * {cantidad_positivos} números positivos
            * {cantidad_negativos} números negativos
            * {cantidad_pares} números pares
            * {cantidad_impares} números impares
    """)

def actividad_9():
    # 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
    # media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
    # poder procesar 100 números cambiando solo un valor).
    cantidad_valores = 10
    valores = [int(input(f"Ingresa un número entero ({i+1} de {cantidad_valores}): ")) for i in range(cantidad_valores)]
    print(f"La media de todos los valores ingresados es {statistics.mean(valores)}")

def actividad_10():
    # 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
    # usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
    numero_ingresado = numero_original = int(input("Ingresa un número entero para invertirlo: "))
    numero_invertido = 0
    while numero_ingresado > 0:
        numero_invertido = (numero_invertido * 10) + (numero_ingresado % 10)
        numero_ingresado = numero_ingresado // 10
    print(f"{numero_invertido} es el número {numero_original} invertido")

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
            '10': actividad_10,
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


