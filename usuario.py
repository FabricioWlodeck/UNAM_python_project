from persona import Persona


class Usuario(Persona):
    def __init__(self,nombre, apellido, edad, tipo_suscripcion):
        #cambie Persona().__init__  por super().__init__
        super().__init__(nombre, apellido, edad)
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
        texto = (f'{self.nombre}, {self.apellido} \nSuscripcion: {self.tipo_suscripcion.tipo}')
        return texto

    def listado_libros_usuario(self):
        contador = 1 
        print(f'\n---LIBROS RETIRADOS POR {self.nombre} {self.apellido}---')
        for libros in self.__libros_retirados:
            print(f'{libros} - ')
            contador += contador