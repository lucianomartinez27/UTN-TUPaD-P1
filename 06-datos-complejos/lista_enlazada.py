class Nodo:
    def __init__(self, dato, siguiente=None):
        self.valor = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.final = None

    def insertar(self, dato):
        self.final =  Nodo(dato, self.final)

    def mostrar(self):
        actual = self.final
        cadena = ""
        while actual:
            cadena += f"{actual.valor} ->️ "
            actual = actual.siguiente
        cadena += "None"
        return cadena

    def invertir(self):
        nueva_lista = ListaEnlazada()
        actual = self.final
        while actual:
            nueva_lista.insertar(actual.valor)
            actual = actual.siguiente
        return nueva_lista