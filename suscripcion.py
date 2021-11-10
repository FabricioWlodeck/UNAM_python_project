class Suscripcion():
    def __init__(self, tipo_suscripcion, costo_suscripcion, duracion_suscripcion, requerimiento, libros_para_retirar, fecha_suscripcion, fecha_vencimiento, cantidad_usuarios):
        self.__tipo_suscripcion = tipo_suscripcion
        self.__costo_suscripcion = costo_suscripcion
        self.__duracion_suscripcion = duracion_suscripcion
        self.__requerimientos = []
        self.__libros_para_retirar = libros_para_retirar
        self.__fecha_suscripcion = fecha_suscripcion
        self.__fecha_vencimiento = fecha_vencimiento
        self.__cantidad_usuarios = cantidad_usuarios
