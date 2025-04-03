# Práctico N3 - Estructuras Condicionales
# Alumno: Martinez Luciano Joaquin

import random
from statistics import mode, median, mean
def actividad_1():
    # 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
    # deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad")
def actividad_2():
    # 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
    # mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
    # mensaje “Desaprobado”.

    nota = int(input("Ingrese una nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def actividad_3():
    # 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
    # número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
    # contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
    # operador de módulo (%) en Python para evaluar si un número es par o impar

    numero_ingresado = int(input("Ingrese un número par: "))

    es_par = numero_ingresado % 2 == 0
    if es_par:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
def actividad_4():
    # 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
    # siguientes categorías pertenece:
    # ● Niño/a: menor de 12 años.
    # ● Adolescente: mayor o igual que 12 años y menor que 18 años.
    # ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    # ● Adulto/a: mayor o igual que 30 años

    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Es niño/a")
    elif edad <= 18:
        print("Es adolescente")
    elif edad <= 30:
        print("Es adulto joven")
    else:
        print("Es adulto")

def actividad_5():
    # 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
    # (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
    # pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
    # pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
    # de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
    # como una lista o un string.

    contrasenia = input("Ingrese su contraseña: ")

    if len(contrasenia) in range(8, 15):
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8  y 14 caracteres")

def actividad_6():
    # 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
    # y calcular la moda, la mediana y la media de dichos números.
    # Escribir un programa que tome la lista
    # numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
    # hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

    numeros_aleatorios = [random.randint(1, 100)]

    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)

    if (media > mediana) and (mediana > moda):
        print("Hay sesgo positivo o a la derecha")
    elif (media < mediana) and media < moda:
        print("Hay sesgo negativo o a la derecha")
    else:
        print("No hay sesgo")

def actividad_7():
    # 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
    # termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
    # pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
    # pantalla

    frase_o_palabra = input("Ingrese una frase o palabra: ")

    ultima_letra = frase_o_palabra.lower()[-1]
    if ultima_letra in ['a', 'e', 'i', 'o', 'u']:
        frase_o_palabra += "!"

    print(frase_o_palabra)

def actividad_8():
    # 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
    # dependiendo de la opción que desee:
    # 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    # 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    # 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro

    nombre = input("Ingrese su nombre: ")
    opcion = input(""" 
    Ingrese el número 1, 2 o 3 según la opción que quera:
    
    1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
    
    """)

    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "e":
        print(nombre.title())
    else:
        print("Opción incorrecta")



def actividad_9():
    # 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
    # magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
    # por pantalla:
    # ● Menor que 3: "Muy leve" (imperceptible).
    # ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
    # ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
    # generalmente no causa daños).
    # ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
    # débiles).
    # ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
    # ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
    magnitud_terremoto = int(input("Ingrese la magnitud del terremoto: "))
    if magnitud_terremoto < 3:
        print("Muy leve")
    elif magnitud_terremoto < 4:
        print("Leve")
    elif magnitud_terremoto < 5:
        print("Moderado")
    elif magnitud_terremoto < 6:
        print("Fuerte")
    elif magnitud_terremoto < 7:
        print("Muy fuerte")
    else:
        print("Extremo")


def es_comienzo_o_fin_de_estacion(numero_mes, numero_dia, mes_comienzo_estacion, mes_final_estacion):
    esta_dentro_del_comienzo_de_estacion = (numero_mes == mes_comienzo_estacion and numero_dia >= 21)
    esta_dentro_del_final_de_la_estacion = (numero_mes == mes_final_estacion and numero_dia <= 20)
    return esta_dentro_del_comienzo_de_estacion or esta_dentro_del_final_de_la_estacion

def obtener_periodo(mes, dia):
    enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre = range(1,13)
    # Condición un poco compleja, pero sin usar librerías es lo más simple que se me ocurrió
    periodo_1 = (mes in [enero, febrero]) or es_comienzo_o_fin_de_estacion(mes, dia, diciembre, marzo)
    periodo_2 = (mes in [abril, mayo]) or es_comienzo_o_fin_de_estacion(mes, dia, marzo, junio)
    periodo_3 = (mes in [julio, agosto]) or es_comienzo_o_fin_de_estacion(mes, dia, junio, septiembre)
    periodo_4 = (mes in [septiembre, octubre]) or es_comienzo_o_fin_de_estacion(mes, dia, septiembre, diciembre)
    if periodo_1:
        return 1
    elif periodo_2:
        return 2
    elif periodo_3:
        return 3
    elif periodo_4:
        return 4



def actividad_10():
    # Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
    # del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
    # si el usuario se encuentra en otoño, invierno, primavera o verano.

    hemisferio = input("Ingrese en qué hemisferio se encuentra N/S: ").upper()
    estaciones_hemisferio = {
        'N' : ["Invierno", "Primavera", "Verano", "Otoño"],
        'S': ["Verano", "Otoño", "Invierno", "Primavera"]
    }
    if hemisferio not in ["N", "S"]:
        return print("Ingresaste un dato incorrecto")

    numero_mes = int(input("Ingrese el número de mes actual: "))
    numero_dia = int(input("Ingrese el número de día actual: "))
    es_fecha_valida = numero_mes in range(1, 13) and numero_dia in range(1, 31)
    if not es_fecha_valida:
        return print("Ingresaste un dato incorrecto")

    print(f"Es {estaciones_hemisferio[hemisferio][obtener_periodo(numero_mes, numero_dia) - 1]}")

if __name__ == '__main__':
    def eligir_actividad():
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
            return lambda : None
    actividad = eligir_actividad()
    while actividad is not None:
        actividad()
        actividad = eligir_actividad()
    print("Saló de la aplicación")

