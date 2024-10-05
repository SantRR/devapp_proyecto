from Model.conexion import Conexion
from Model.producto_base import ProductoBase
import sys

def main():
    producto_base = ProductoBase()
    """
    producto_base.producto.clave       = "SKU-31"
    producto_base.producto.descripcion = "Papitas" 
    producto_base.producto.existencia  = 10
    producto_base.producto.precio      = 32
    """
    producto_base.contar_producto()
    return
    
if __name__ == "__main__":
    main()
