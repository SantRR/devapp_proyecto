from Model.control import ControladorVentanas
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorVentanas()
    controlador.show_login()
    sys.exit(app.exec())
