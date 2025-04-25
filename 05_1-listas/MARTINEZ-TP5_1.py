# Práctico N5.1 - Listas
# Alumno: Martinez Luciano Joaquin


def actividad_1():
    # 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
    # range.
    print(list(range(4, 101, 4)))

def actividad_2():
    # 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
    # penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
    # indexing con números negativos!
    lista = ["A", "B", "C", "D", "E"]
    print(lista[-2])

def actividad_3():
    # 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
    # pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
    # ejemplo:
    lista = []
    lista.append("Python")
    lista.append("UTN")
    lista.append("Programación")
    print(lista)


def actividad_4():
    # 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
    # respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
    # en los videos o bien investigar cómo funciona el indexing con números negativos!
    # animales = ["perro", "gato", "conejo", "pez"]
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print(animales)


def actividad_5():
    # 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
    numeros = [8, 15, 3, 22, 7] # define una lista de números enteros
    numeros.remove(max(numeros)) # obtiene el mayor (en este caso 22) y lo elimina de la lista
    print(numeros) # imprime la lista

def actividad_6():
    # 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
    # pantalla los dos primeros
    lista = list(range(10, 31, 5))
    print(lista[0:2])


def actividad_7():
    # 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
    # cualesquiera.
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1] = "BMW"
    autos[2] = "Ferrari"
    print(autos)


def actividad_8():
    # 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print(dobles)


def actividad_9():
    # 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
    # diferentes clientes:
    # compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
    # ["agua"]]
    # a) Agregar "jugo" a la lista del tercer cliente usando append.
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    # c) Eliminar "pan" de la lista del primer cliente.
    # d) Imprimir la lista resultante por pantalla
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print(compras)


def actividad_10():
    # 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
    # ● Posición lista_anidada[0]: 15
    # ● Posición lista_anidada[1]: True
    # ● Posición lista_anidada[2][0]: 25.5
    # ● Posición lista_anidada[2][1]: 57.9
    # ● Posición lista_anidada[2][2]: 30.6
    # ● Posición lista_anidada[3]: False
    # Imprimir la lista resultante por pantalla.
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print(lista_anidada)


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
    print("Salió de la aplicación")



