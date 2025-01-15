from bdd.data import DataLayer

class BusinessLayer:
    @staticmethod
    def consultar_producto(id_producto):
        if not isinstance(id_producto, int) or id_producto <= 0:
            return {"error": "ID de producto debe ser un entero positivo."}
        producto = DataLayer.obtener_producto(id_producto)
        if not producto:
            return {"error": "Producto no encontrado."}
        return producto

    @staticmethod
    def agregar_producto(id_producto, cantidad):
        if not isinstance(id_producto, int) or id_producto <= 0:
            return {"error": "ID de producto debe ser un entero positivo."}
        if not isinstance(cantidad, int) or cantidad <= 0:
            return {"error": "Cantidad debe ser un entero positivo."}
        if DataLayer.obtener_producto(id_producto):
            return {"error": "El producto ya existe."}
        nombre_producto = f"Producto {id_producto}"
        DataLayer.agregar_producto(id_producto, nombre_producto, cantidad)
        return {"mensaje": "Producto agregado exitosamente."}

    @staticmethod
    def actualizar_stock(id_producto, nueva_cantidad):
        assert isinstance(id_producto, int) and id_producto > 0, "ID de producto debe ser un entero positivo."
        assert isinstance(nueva_cantidad, int) and nueva_cantidad >= 0, "Nueva cantidad debe ser un entero no negativo."

        producto = DataLayer.obtener_producto(id_producto)
        if not producto:
            raise ValueError("Producto no encontrado.")

        DataLayer.actualizar_stock(id_producto, nueva_cantidad)
        return {"mensaje": "Stock actualizado exitosamente."}

