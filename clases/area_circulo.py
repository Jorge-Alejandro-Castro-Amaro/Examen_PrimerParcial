import math

class AreaCirculo:
    def __init__(self, radio):
        self.radio = radio
        self.a = 0

    def calcular_area(self):
        self.a = (math.pi * (self.radio ** 2))
    