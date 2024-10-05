import pyodbc  # type: ignore

class Conexion():
    def __init__(self):
        self.conexion = ""
    
    def establecer_conexion(self):
        try:
            self.conexion = pyodbc.connect(r"DRIVER={SQL Server};SERVER=SANT\SQLEXPRESS01;DATABASE=bdsistema;Trusted_Connection=yes")
            print("conexion establecida")
        except Exception as ex:
            print("no se pudo establecer conexion")
            print("error:", ex)
        return
    
    def cerrar_conexion(self):
        self.conexion.close()
        return
