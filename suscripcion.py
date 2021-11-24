# ELIMINAR HERENCIA Y SIMPLEMENTE INSTANCIA UNO PARA ALUMNO Y OTRO PARA ESTANDAR
class Suscripcion():
    def __init__(self, costo_suscripcion=500, duracion_suscripcion=None, libros_para_retirar=5, fecha_suscripcion=None, fecha_vencimiento=None, tipo=None):
        self.__costo_suscripcion = costo_suscripcion
        self.__duracion_suscripcion = duracion_suscripcion
        self.__libros_para_retirar = libros_para_retirar
        self.__fecha_suscripcion = fecha_suscripcion
        self.__fecha_vencimiento = fecha_vencimiento
        self.__tipo = tipo

    @property
    def costo_suscripcion(self):
        return self.__costo_suscripcion

    @costo_suscripcion.setter
    def costo_suscripcion(self, value):
        self.__costo_suscripcion = value

    @property
    def duracion_suscripcion(self):
        return self.__duracion_suscripcion

    @duracion_suscripcion.setter
    def duracion_suscripcion(self, value):
        self.__duracion_suscripcion = value

    @property
    def libros_para_retirar(self):
        return self.__libros_para_retirar

    @libros_para_retirar.setter
    def libros_para_retirar(self, value):
        self.__libros_para_retirar = value

    @property
    def fecha_suscripcion(self):
        return self.__fecha_suscripcion

    @fecha_suscripcion.setter
    def fecha_suscripcion(self, value):
        self.__fecha_suscripcion = value

    @property
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, value):
        self.__fecha_vencimiento = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    def __srt__(self):
        texto = (f'Tipo de suscripcion: {self.__tipo}')
        return texto
