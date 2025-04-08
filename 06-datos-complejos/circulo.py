import math


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def calcular_area(self):
        return math.pi * self.radio ** 2