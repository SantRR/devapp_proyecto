# from Model.load_login import LoadLogin
from Model.producto_base import ProductoBase
from PyQt6.QtWidgets import QMainWindow, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import uic, QtCore
import os, sys

class LoadMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializar_main()
        return
    
    def inicializar_main(self):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(directorio_actual)
        directorio_main = os.path.join(directorio_actual, "../ui/main.ui")
        self.main = uic.loadUi(directorio_main, self)
        
        self.main.setFixedSize(900, 720)
        self.setWindowTitle("Main administrador inventario")
        
        self.main.tbl_mostrar_productos.setVerticalHeader(QHeaderView(QtCore.Qt.Orientation.Vertical))
        self.main.tbl_mostrar_productos.verticalHeader().setVisible(False)
        
        self.main.btn_agregar.clicked.connect(self.on_click_btn_agregar)
        self.main.btn_modificar.clicked.connect(self.on_click_btn_modificar)
        self.main.btn_eliminar.clicked.connect(self.on_click_btn_eliminar)
        self.main.btn_mostrar.clicked.connect(self.on_click_btn_mostrar)
        self.main.btn_salir.clicked.connect(self.on_click_btn_salir)
        
        self.on_click_btn_mostrar()
        return
        
    def on_click_btn_modificar(self):
        if self.validar_valores():
            clave, descripcion, existencia, precio = self.obtener_valores_reales()
            producto_base = ProductoBase()
            producto_base.producto.clave       = clave
            producto_base.producto.descripcion = descripcion
            producto_base.producto.existencia  = existencia
            producto_base.producto.precio      = precio
            producto_base.modificar_producto()
            self.limpiar_lbls()
            self.on_click_btn_mostrar()
            return
        else:
            
            return
    
    def on_click_btn_eliminar(self):
        clave = self.main.txt_clave.text()
        if clave:
            producto_base = ProductoBase()
            id_producto = producto_base.obtener_id_por_clave(clave)
            producto_base.producto.id_producto = id_producto
            producto_base.eliminar_producto()
            self.limpiar_lbls()
            self.on_click_btn_mostrar()
        return
    
    def on_click_btn_agregar(self):
        if self.validar_valores():
            clave, descripcion, existencia, precio = self.obtener_valores_reales()
            producto_base = ProductoBase()
            producto_base.producto.clave       = clave
            producto_base.producto.descripcion = descripcion
            producto_base.producto.existencia  = existencia
            producto_base.producto.precio      = precio
            producto_base.agregar_producto()
            self.limpiar_lbls()
            self.on_click_btn_mostrar()
            return
        else:
            return
    
    def on_click_btn_mostrar(self):
        modelo_tabla = QStandardItemModel()
        encabezados = ["ID producto", "Clave", "Descripción", "Existencia", "Precio"]
        modelo_tabla.setHorizontalHeaderLabels(encabezados)
        producto_base = ProductoBase()
        productos = producto_base.lista_producto()
        for producto in productos:
            fila = [
                QStandardItem(str(producto["id_producto"])),
                QStandardItem(producto["clave"]),
                QStandardItem(producto["descripcion"]),
                QStandardItem(str(producto["existencia"])),
                QStandardItem(f"{producto["precio"]:.2f}")
            ]
            modelo_tabla.appendRow(fila)
        self.main.tbl_mostrar_productos.setModel(modelo_tabla)
        self.main.tbl_mostrar_productos.setColumnWidth(0, 104)  # Ancho para la columna de ID
        self.main.tbl_mostrar_productos.setColumnWidth(1, 104)  # Ancho para la columna de clave
        self.main.tbl_mostrar_productos.setColumnWidth(2, 328)  # Ancho para la columna de descripción
        self.main.tbl_mostrar_productos.setColumnWidth(3, 104)  # Ancho para la columna de existencia
        self.main.tbl_mostrar_productos.setColumnWidth(4, 104)  # Ancho para la columna de precio
        return
    
    def obtener_valores_str(self):
        clave_str       = self.main.txt_clave.text()        # str
        descripcion_str = self.main.txt_descripcion.text()  # str
        existencia_str  = self.main.txt_existencia.text()   # int
        precio_str      = self.main.txt_precio.text()       # float
        return clave_str, descripcion_str, existencia_str, precio_str
    
    def validar_valores(self):
        clave_str, descripcion_str, existencia_str, precio_str = self.obtener_valores_str()
        try:
            existencia_int = int(existencia_str)
            valido_exis = True
        except ValueError:
            self.main.txt_clave.setText("")
            self.main.txt_descripcion.setText("")
            self.main.txt_existencia.setText("Error")
            valido_exis = False
        try:
            precio_float = float(precio_str)
            valido_precio = True
        except ValueError:
            self.main.txt_clave.setText("")
            self.main.txt_descripcion.setText("")
            self.main.txt_precio.setText("Error")
            valido_precio = False
        if (valido_exis and valido_precio): return True, existencia_int, precio_float
        else: return False
    
    def obtener_valores_reales(self):
        clave_str, descripcion_str, existencia_str, precio_str = self.obtener_valores_str()
        existencia_int = int(existencia_str)
        precio_float = float(precio_str)
        return clave_str, descripcion_str, existencia_int, precio_float
    
    def limpiar_lbls(self):
        self.main.txt_clave.setText("")
        self.main.txt_descripcion.setText("")
        self.main.txt_existencia.setText("")
        self.main.txt_precio.setText("")
        
    def on_click_btn_salir(self):
        self.main.close()
        # self.login = LoadLogin()
        # self.login.show()
        return