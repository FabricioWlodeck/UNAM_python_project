from suscripcion import Suscripcion


# requerimientos = {'certicado_alumno': True, }
class Suscripcion_estandar(Suscripcion):
    def __init__(self, costo_suscripcion=None, duracion_suscripcion=None, libros_para_retirar=None, fecha_suscripcion=None, fecha_vencimiento=None, cantidad_usuarios=None):
        Suscripcion.__init__(self, costo_suscripcion, duracion_suscripcion, libros_para_retirar, fecha_suscripcion, fecha_vencimiento, cantidad_usuarios)
        self.__costo_suscripcion = 750 # $750
        self.__requerimiento_es_alumno = False

    @property
    def requerimientos_es_alumno(self):
        return self.__requerimiento_es_alumno
    
    @requerimientos_es_alumno.setter
    def requerimientos_es_alumno(self,value):
        self.__requerimiento_es_alumno = value

    def __str__(self):
        texto = (f'Suscripcion estandar para cualquier tipo de lector')
        return texto