from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Lista donde se van a almacenar los clientes
clientes = []

# Función para cargar los clientes desde el archivo json si existe
def cargar_clientes():
    if os.path.exists('clientes.json'):
        with open('clientes.json', 'r') as file:
            return json.load(file)
    return []

# Ruta principal para el formulario de registro
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        nit = request.form['nit']

        clientes.append({'nombre': nombre, 'correo': correo, 'nit': nit})

        # Guardar clientes en archivo json
        with open('clientes.json', 'w') as file:
            json.dump(clientes, file)

        return render_template('index.html', mensaje='Cliente registrado con éxito.', mostrar_tabla=False)
    else:
        return render_template('index.html', mostrar_tabla=False)

# Ruta para obtener los clientes
@app.route('/getClientes', methods=['GET'])
def get_clientes():
    clientes_data = cargar_clientes()
    return render_template('index.html', clientes=clientes_data, mostrar_tabla=True)

if __name__ == '__main__':
    app.run(debug=True)
