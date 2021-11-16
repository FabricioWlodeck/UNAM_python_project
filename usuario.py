from persona import Persona


class Usuario(Persona):
    def __init__(self, nombre_cuenta, contrasenia, nombre, apellido, edad, tipo_suscripcion):
        #cambie Persona().__init__  por super().__init__
        super().__init__(nombre_cuenta, contrasenia, nombre, apellido, edad)
        self.__tipo_suscripcion = tipo_suscripcion
        self.__libros_retirados = []  # se le pasara objetos tipo libro

    @property
    def tipo_suscripcion(self):
        return self.__tipo_suscripcion

    @tipo_suscripcion.setter
    def tipo_suscripcion(self,value):
        self.__tipo_suscripcion = value

    @property
    def libros_retirados(self):
        return self.__libros_retirados

    @libros_retirados.setter
    def libros_retirados(self,value):
        self.__libros_retirados = value

    def __str__(self):
        texto = (f'{self.nombre}, {self.apellido}')
        return texto

    def listado_libros(self):
        contador = 1 
        print(f'---LIBROS RETIRADOS POR {self.nombre_cuenta}---')
        for libros in self.__libros_retirados:
            print(f'({contador}) {libros}')
            contador += contador