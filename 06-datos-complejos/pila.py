class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_tope(self):
        return self.elementos[-1] if not self.esta_vacia() else None