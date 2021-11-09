from persona import Persona


class Empleado(Persona):
    def __init__(self, nombre_usuario, contrasenia, nombre, apellido, edad, horario, cargo, sueldo):
        Persona().__init__(nombre_usuario, contrasenia, nombre, apellido, edad)
        self.__horario = horario
        self.__cargo = cargo
        self.__sueldo = sueldo

