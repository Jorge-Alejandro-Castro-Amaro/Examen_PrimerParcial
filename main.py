import sys
from PyQt5.QtWidgets import QApplication
from clases_load.load_menu_principal import LoadMenuPrincipal

def main():
    app = QApplication(sys.argv)
    menu_principal = LoadMenuPrincipal()
    menu_principal.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()