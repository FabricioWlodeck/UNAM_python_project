from suscripcion import Suscripcion


# requerimientos = {'certicado_alumno': True, }
class Suscripcion_alumno(Suscripcion):
    def __init__(self, costo_suscripcion=500, duracion_suscripcion= 12, libros_para_retirar= 5, fecha_suscripcion=None, fecha_vencimiento=None, cantidad_usuarios=None):
        Suscripcion.__init__(self, costo_suscripcion, duracion_suscripcion, libros_para_retirar, fecha_suscripcion, fecha_vencimiento, cantidad_usuarios)
        self.__requerimiento_es_alumno = True

    @property
    def requerimientos_es_alumno(self):
        return self.__requerimiento_es_alumno
    
    @requerimientos_es_alumno.setter
    def requerimientos_es_alumno(self,value):
        self.__requerimiento_es_alumno = value

    def __str__(self):
        texto = print(f'Suscripcion exclusiva para estudiantes')
        return texto