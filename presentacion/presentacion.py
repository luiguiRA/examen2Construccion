from flask import Flask, request, jsonify
from controlador.negocio import BusinessLayer

app = Flask(__name__)

@app.route('/producto/<int:id_producto>', methods=['GET'])
def api_consultar_producto(id_producto):
    resultado = BusinessLayer.consultar_producto(id_producto)
    if "error" in resultado:
        return jsonify(resultado), 400
    return jsonify(resultado), 200

@app.route('/producto', methods=['POST'])
def api_agregar_producto():
    datos = request.json
    if not datos or "id_producto" not in datos or "cantidad" not in datos:
        return jsonify({"error": "Datos incompletos."}), 400
    resultado = BusinessLayer.agregar_producto(datos["id_producto"], datos["cantidad"])
    if "error" in resultado:
        return jsonify(resultado), 400
    return jsonify(resultado), 201

@app.route('/producto/<int:id_producto>', methods=['PUT'])
def api_actualizar_stock(id_producto):
    datos = request.json
    if not datos or "nueva_cantidad" not in datos:
        return jsonify({"error": "Datos incompletos."}), 400
    try:
        resultado = BusinessLayer.actualizar_stock(id_producto, datos["nueva_cantidad"])
        return jsonify(resultado), 200
    except AssertionError as e:
        return jsonify({"error": str(e)}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
