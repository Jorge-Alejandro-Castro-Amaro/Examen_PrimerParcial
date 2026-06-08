import sys
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.area_circulo import AreaCirculo

class LoadACirculo(QDialog):
    def __init__(self):
        super(). __init__()
        self.ui = uic.loadUi("ui/area_circulo.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_area)

    def calcular_area(self):
        radio = float(self.txt_radio.text())
        circulo = AreaCirculo(radio)
        circulo.calcular_area()
        self.lbl_resultado.setText(f"El área del círculo es: {circulo.a}")
        