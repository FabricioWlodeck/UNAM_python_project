from persona import Persona

class Usuario(Persona):
    def __init__(self, nombre_usuario, contrasenia, nombre, apellido, edad, tipo_suscripcion, libros_retirados):
        Persona().__init__(nombre_usuario, contrasenia, nombre, apellido, edad)
        self.__tipo_suscripcion = tipo_suscripcion
        self.__libros_retirados = [] # se le pasara objetos tipo libro
