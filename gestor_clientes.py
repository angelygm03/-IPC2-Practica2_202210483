import json
import os

class GestorClientes:
    def __init__(self):
        self.clientes = []

    def cargar_clientes(self):
        if os.path.exists('clientes.json'):
            with open('clientes.json', 'r') as file:
                self.clientes = json.load(file)
        else:
            self.clientes = []

    def guardar_clientes(self):
        with open('clientes.json', 'w') as file:
            json.dump(self.clientes, file)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def obtener_clientes(self):
        return self.clientes
