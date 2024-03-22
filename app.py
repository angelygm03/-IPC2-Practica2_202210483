from flask import Flask, render_template, request
from cliente import Cliente
from gestor_clientes import GestorClientes

app = Flask(__name__)
gestor = GestorClientes()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        nit = request.form['nit']

        gestor.cargar_clientes()

        # Se verifica si el nit ya está registrado
        nits_registrados = [cliente['nit'] for cliente in gestor.obtener_clientes()]
        if nit in nits_registrados:
            return render_template('index.html', mensaje='¡Error! Este NIT ya está registrado.', mostrar_tabla=False)

        # Si el nit no existe se agrega el cliente a la lista
        nuevo_cliente = Cliente(nombre, correo, nit)
        gestor.agregar_cliente(nuevo_cliente.__dict__)
        gestor.guardar_clientes()

        return render_template('index.html', mensaje='Cliente registrado con éxito.', mostrar_tabla=False)
    else:
        return render_template('index.html', mostrar_tabla=False)

@app.route('/getClientes', methods=['GET'])
def get_clientes():
    gestor.cargar_clientes()
    return render_template('index.html', clientes=gestor.obtener_clientes(), mostrar_tabla=True)

if __name__ == '__main__':
    app.run(debug=True)
