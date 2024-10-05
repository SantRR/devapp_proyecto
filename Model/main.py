from Model.load_login import LoadLogin
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = LoadLogin()
    ventana.show()
    sys.exit(app.exec())
