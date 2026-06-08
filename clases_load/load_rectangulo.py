import sys
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.area_rectangulo import AreaRectangulo

class LoadARectangulo(QDialog):
    def __init__(self):
        super(). __init__()
        self.ui = uic.loadUi("ui/area_rectangulo.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_area)

    def calcular_area(self):
        base = float(self.txt_base.text())
        altura = float(self.txt_altura.text())
        rectangulo = AreaRectangulo(base, altura)
        rectangulo.calcular_area()
        self.lbl_resultado.setText(f"El área del rectángulo es: {rectangulo.a}")
        