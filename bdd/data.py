from flask import Flask, jsonify, request

app = Flask(__name__)

# Capa de datos
class DataLayer:
    database = {
        1: {"nombre": "Producto A", "stock": 50},
        2: {"nombre": "Producto B", "stock": 30},
    }

    @staticmethod
    def obtener_producto(id_producto):
        return DataLayer.database.get(id_producto)

    @staticmethod
    def agregar_producto(id_producto, nombre, cantidad):
        DataLayer.database[id_producto] = {"nombre": nombre, "stock": cantidad}

    @staticmethod
    def actualizar_stock(id_producto, nueva_cantidad):
        if id_producto in DataLayer.database:
            DataLayer.database[id_producto]["stock"] = nueva_cantidad

# Endpoint para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_todos_los_productos():
    return jsonify(DataLayer.database), 200

if __name__ == '__main__':
    app.run(debug=True)
