class Cliente:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.validar_nit(nit)

    def validar_nit(self, nit):
        try:
            nit_entero = int(nit)
            if nit_entero <= 0:
                raise ValueError("El NIT debe ser un entero positivo.")
            self.nit = nit_entero
        except ValueError:
            raise ValueError("El NIT debe ser un entero positivo.")
