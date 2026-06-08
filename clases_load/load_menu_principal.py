from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from clases_load.load_a_triangulo import LoadATriangulo
from clases_load.load_rectangulo import LoadARectangulo
from clases_load.load_a_circulo import LoadACirculo

class LoadMenuPrincipal(QMainWindow):
    def __init__(self):
        super(). __init__()
        self.ui = uic.loadUi("ui/menu_principal.ui", self)
        
        self.actionTriangulo.triggered.connect(self.abrir_area_triangulo)
        self.actionRectangulo.triggered.connect(self.abrir_area_rectangulo)
        self.actionCirculo.triggered.connect(self.abrir_area_circulo)
        self.actionSalir.triggered.connect(self.close)
        
    def abrir_area_triangulo(self):
        self.load_a_triangulo = LoadATriangulo()
        self.load_a_triangulo.show()
    
    def abrir_area_rectangulo(self):
        self.load_a_rectangulo = LoadARectangulo()
        self.load_a_rectangulo.show()
    
    def abrir_area_circulo(self):
        self.load_a_circulo = LoadACirculo()
        self.load_a_circulo.show()