from Model.producto import Producto
from Model.conexion import Conexion

class ProductoBase():
    def __init__(self):
        self.producto = Producto()
        return
    
    def agregar_producto(self):
        basedatos = Conexion()
        basedatos.establecer_conexion()
        sp = "exec [dbo].[sp_insertar_producto] @clave=?, @descripcion=?, @existencia=?, @precio=?"
        params = (self.producto.clave, self.producto.descripcion, self.producto.existencia, self.producto.precio) 
        cursor = basedatos.conexion.cursor()
        cursor.execute(sp, params)
        cursor.commit()
        basedatos.cerrar_conexion()
        return
    
    def modificar_producto(self):
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
        basedatos.cerrar_conexion()
        return cantidad[0]
    
    def lista_producto(self):
        basedatos = Conexion()
        basedatos.establecer_conexion()
        cursor = basedatos.conexion.cursor()
        sp = "exec [dbo].[sp_listar_productos]"
        cursor.execute(sp)
        filas = cursor.fetchall()
        lista_productos = []
        for fila in filas:
            producto = {
                "id_producto": fila[0],
                "clave": fila[1],
                "descripcion": fila[2],
                "existencia": fila[3],
                "precio": fila[4]
            }
            lista_productos.append(producto)
        basedatos.cerrar_conexion()
        return lista_productos

    def obtener_id_por_clave(self, clave):
        basedatos = Conexion()
        basedatos.establecer_conexion()
        cursor = basedatos.conexion.cursor()
        params = (clave,)
        consulta = "SELECT [dbo].[fn_obtener_id_producto_por_clave](?)"
        cursor.execute(consulta, params)
        resultado = cursor.fetchone()
        basedatos.cerrar_conexion()
        if resultado:
            return resultado[0]
        else:
            return None
