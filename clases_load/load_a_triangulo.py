import sys
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.area_triangulo import AreaTriangulo

class LoadATriangulo(QDialog):
    def __init__(self):
        super(). __init__()
        self.ui = uic.loadUi("ui/area_trianuglo.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_area)

    def calcular_area(self):
        base = float(self.txt_base.text())
        altura = float(self.txt_altura.text())
        triangulo = AreaTriangulo(base, altura)
        triangulo.calcular_area()
        self.lbl_resultado.setText(f"El área del triángulo es: {triangulo.c}")