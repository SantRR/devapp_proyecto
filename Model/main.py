# from Model.load_login import LoadLogin
from Model.load_main import LoadMain
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #ventana = LoadLogin()
    ventana = LoadMain()
    ventana.show()
    sys.exit(app.exec())
