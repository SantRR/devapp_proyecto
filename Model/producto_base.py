from tienda.model.base.producto import Producto
from tienda.model.conexion import Conexion

class ProductoBase():
    def __init__(self):
        self.producto = Producto()
        return
    
    def guardar_producto(self):
        basedatos = Conexion()
        basedatos.establecer_conexion()
        sp = "exec [dbo].[sp_insertar_producto] @clave=?, @descripcion=?, @existencia=?, @precio=?"
        params = (self.producto.clave, self.producto.descripcion, self.producto.existencia, self.producto.precio) 
        cursor = basedatos.conexion.cursor()
        cursor.execute(sp, params)
        cursor.commit()
        basedatos.cerrar_conexion()
        return
    
    def actualizar_producto(self):
        basedatos = Conexion()
        basedatos.establecer_conexion()
        sp = "exec [dbo].[sp_actualizar_producto] @id_producto=?, @clave=?, @descripcion=?, @existencia=?, @precio=?"
        params = (self.producto.id_producto, self.producto.clave, self.producto.descripcion, self.producto.existencia, self.producto.precio) 
        cursor = basedatos.conexion.cursor()
        cursor.execute(sp, params)
        cursor.commit()
        basedatos.cerrar_conexion()
        return
    
    def eliminar_producto(self):
        basedatos = Conexion()
        basedatos.establecer_conexion()
        sp = "exec [dbo].[sp_eliminar_producto] @id_producto=?"
        params = (self.producto.id_producto) 
        cursor = basedatos.conexion.cursor()
        cursor.execute(sp, params)
        cursor.commit()
        basedatos.cerrar_conexion()
        return
    
    def contar_producto(self):
        basedatos = Conexion()
        basedatos.establecer_conexion()
        fn = "SELECT [dbo].[fn_contar_productos]()"
        cursor = basedatos.conexion.cursor()
        cursor.execute(fn)
        cantidad = cursor.fetchone()
        print(cantidad[0])
        cursor.commit()
        basedatos.cerrar_conexion()
        return
    
    def lista_producto(self):
        basedatos = Conexion()
        basedatos.establecer_conexion()
        cursor = basedatos.conexion.cursor()
        sp = "exec [dbo].[sp_listar_productos]"
        cursor.execute(sp)
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)
        basedatos.cerrar_conexion()
        return
