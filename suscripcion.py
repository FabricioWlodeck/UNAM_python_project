class Suscripcion():
    def __init__(self, costo_suscripcion, duracion_suscripcion,  libros_para_retirar, fecha_suscripcion, fecha_vencimiento):
        self.__costo_suscripcion = costo_suscripcion
        self.__duracion_suscripcion = duracion_suscripcion
        self.__libros_para_retirar = libros_para_retirar
        self.__fecha_suscripcion = fecha_suscripcion
        self.__fecha_vencimiento = fecha_vencimiento
        

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

