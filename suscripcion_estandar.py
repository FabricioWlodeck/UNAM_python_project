from suscripcion import Suscripcion
#from usuario import Usuario


class Suscripcion_estandar(Suscripcion):
    def __init__(self, costo_suscripcion=None, duracion_suscripcion=None, libros_para_retirar=None, fecha_suscripcion=None, fecha_vencimiento=None):
        Suscripcion.__init__(self, costo_suscripcion, duracion_suscripcion, libros_para_retirar, fecha_suscripcion, fecha_vencimiento)
        self.__costo_suscripcion = 750 # $750
        self.__requerimiento_es_alumno = False
        self.__lista_usuarios = []

    @property
    def costo_suscripcion(self):
        return self.__costo_suscripcion

    @costo_suscripcion.setter
    def costo_suscripcion(self, value):
        self.__costo_suscripcion = value

    @property
    def requerimientos_es_alumno(self):
        return self.__requerimiento_es_alumno
    
    @requerimientos_es_alumno.setter
    def requerimientos_es_alumno(self,value):
        self.__requerimiento_es_alumno = value
    
    @property
    def lista_usuarios(self):
        return self.__lista_usuarios

    @lista_usuarios.setter
    def lista_usuarios(self, value):
        self.__lista_usuarios = value

    def __str__(self):
        texto = (f'Suscripcion de lector estandar')
        return texto

    """ def suscribir_usuario(self,usuario):
        self.__lista_usuarios.append(usuario)

    def desuscribir_usuario(self,usuario):
        self.__lista_usuarios.remove(usuario) """