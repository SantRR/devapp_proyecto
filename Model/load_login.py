from Model.control import ControladorVentanas
from PyQt6.QtWidgets import QDialog
from PyQt6 import uic
import os, sys

class LoadLogin(QDialog):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.inicializar_login()
        return
    
    def inicializar_login(self):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(directorio_actual)
        directorio_login = os.path.join(directorio_actual, "../ui/login.ui")
        self.login = uic.loadUi(directorio_login, self)
        self.login.setFixedSize(600, 400)
        self.login.btn_ingresar.clicked.connect(self.on_click_btn_ingresar)
        return
    
    def on_click_btn_ingresar(self):
        self.controlador.show_main()
        return
    