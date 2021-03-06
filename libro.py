#ELIMINAR ATRIBUTO CANTIDAD DE LIBRO
class Libro():
    def __init__(self, nombre, autor, edicion, tipo=None):
        self.__nombre = nombre
        self.__autor = autor
        self.__edicion = edicion
        self.__tipo = tipo
        self.__fecha_devolucion = None
        self.__interes_atraso = 15

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        self.__autor = value

    @property
    def edicion(self):
        return self.__edicion

    @edicion.setter
    def edicion(self, value):
        self.__edicion = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @property
    def fecha_devolucion(self):
        return self.__fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, value):
        self.__fecha_devolucion = value

    @property
    def interes_atraso(self):
        return self.__interes_atraso

    @interes_atraso.setter
    def interes_atraso(self, value):
        self.__interes_atraso = value

    def __str__(self):
        texto = (f'{self.__nombre}, {self.__autor} {self.__edicion}')
        return texto
