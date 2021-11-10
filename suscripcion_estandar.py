from suscripcion import Suscripcion


# requerimientos = {'certicado_alumno': True, }
class Suscripcion_estandar(Suscripcion):
    def __init__(self, tipo_suscripcion, costo_suscripcion, duracion_suscripcion, requerimiento, libros_para_retirar, fecha_suscripcion, fecha_vencimiento, cantidad_usuarios):
        Suscripcion.__init__(self, tipo_suscripcion, costo_suscripcion, duracion_suscripcion, requerimiento, libros_para_retirar, fecha_suscripcion, fecha_vencimiento, cantidad_usuarios)
        self.__requerimiento = requerimiento
        self.__