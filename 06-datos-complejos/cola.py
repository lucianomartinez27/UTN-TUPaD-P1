from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        return self.elementos.popleft() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_frente(self):
        return self.elementos[0] if not self.esta_vacia() else None