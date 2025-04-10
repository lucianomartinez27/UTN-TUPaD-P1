# Práctico N6 - Estructuras de datos complejas
# Alumno: Martinez Luciano Joaquin
from time import sleep

from persona import Persona
from circulo import Circulo
from funciones import balanceado
from banco import Banco
from lista_enlazada import ListaEnlazada

def actividad_1():
    # 1) Dado el diccionario precios_frutas
    # precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
    # 1450}
    # Añadir las siguientes frutas con sus respectivos precios:
    # ● Naranja = 1200
    # ● Manzana = 1500
    # ● Pera = 2300
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    print(precios_frutas)
    return precios_frutas

def actividad_2():
    # 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
    # desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
    # ● Banana = 1330
    # ● Manzana = 1700
    # ● Melón = 2800
    precios_frutas = actividad_1()
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    print(precios_frutas)
    return precios_frutas

def actividad_3():
    # 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
    # desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
    # precios.
    precios_frutas = actividad_2()
    lista_frutas = list(precios_frutas.keys())
    print(lista_frutas)
    return lista_frutas

def actividad_4():
    # 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
    # nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
    # mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
    # años."
    luciano = Persona("Luciano", "Argentina", 30)
    print(luciano.saludar())

def actividad_5():
    # 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
    # calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente
    circulo = Circulo(10)
    print(f"Area: {circulo.calcular_area()} - Perimetro: {circulo.calcular_perimetro()}")

def actividad_6():
    # 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
    # balanceados usando una pila.
    print(f"({{[]}}) -> {balanceado("({[]})")}")
    print(f"() -> {balanceado("()")}")
    print(f"({{[}}) -> {balanceado("({[})")}")
    print(f"(}} -> {balanceado("(}")}")

def actividad_7():
    # 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
    # ● Agregar clientes (encolar).
    # ● Atender clientes (desencolar).
    # ● Mostrar el siguiente cliente en la fila.
    banco = Banco()
    banco.agregar_cliente("Luciano")
    sleep(1)
    banco.agregar_cliente("Juan")
    sleep(1)
    banco.atender_cliente()
    sleep(1)
    banco.agregar_cliente("Pedro")
    sleep(1)
    banco.mostrar_siguiente()
    sleep(1)
    banco.atender_cliente()
    sleep(1)
    banco.atender_cliente()

def actividad_8():
    # 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
    # los valores almacenados.
    lista = ListaEnlazada()
    lista.insertar(3)
    lista.insertar(2)
    lista.insertar(1)
    print(lista.mostrar())

def actividad_9():
    # 9) Dada una lista enlazada, implementa una función para invertirla
    lista = ListaEnlazada()
    lista.insertar(3)
    lista.insertar(2)
    lista.insertar(1)
    lista_invertida = lista.invertir()
    print(f"Lista original: {lista.mostrar()}")
    print(f"Lista invertida: {lista_invertida.mostrar()}")

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
        }
        if  numero in actividades:
            return actividades[numero]
        else:
            return None
    actividad = elegir_actividad()
    while actividad is not None:
        actividad()
        actividad = elegir_actividad()
    print("Salió de la aplicación")



