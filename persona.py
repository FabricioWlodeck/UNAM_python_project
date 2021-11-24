class Persona():
    def __init__(self,nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    
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