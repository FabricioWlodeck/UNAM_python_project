class Persona():
    def __init__(self, nombre_cuenta, contrasenia, nombre, apellido, edad):
        self.__nombre_cuenta = nombre_cuenta
        self.__contrasenia = contrasenia
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @property
    def nombre_cuenta(self):
        return self.__nombre_cuenta

    @nombre_cuenta.setter
    def nombre_cuenta(self,value):
        self.__nombre_cuenta = value

    @property
    def contrasenia(self):
        return self.__contrasenia

    @contrasenia.setter
    def contrasenia(self,value):
        self.__contrasenia = value
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,value):
        self.__apellido = value
    
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,value):
        self.__edad = value