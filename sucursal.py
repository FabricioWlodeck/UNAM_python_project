from usuario import Usuario
from libro import Libro
from suscripcion_alumno import Suscripcion_alumno
from suscripcion_estandar import Suscripcion_estandar


class Sucursal():
    def __init__(self, localidad, direccion, personal, horarios_atencion, dinero_recaudado):
        self.localidad = localidad
        self.__direccion = direccion
        self.__personal = personal
        self.__horarios_atencion = horarios_atencion
        self.__dinero_recaudado = dinero_recaudado
        self.__lista_libros = []  # lista de diccionarios de objetos Libro
        self.__usuarios = []  # lista de diccionarios de objetos Usuario

    @property
    def localidad(self):
        return self.__localidad

    @localidad.setter
    def localidad(self, value):
        self.__localidad = value

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @property
    def personal(self):
        return self.__personal

    @personal.setter
    def personal(self, value):
        self.__personal = value

    @property
    def horarios_atencion(self):
        return self.__horarios_atencion

    @horarios_atencion.setter
    def horarios_atencion(self, value):
        self.horarios_atencion = value

    @property
    def dinero_recaudado(self):
        return self.dinero_recaudado

    @dinero_recaudado.setter
    def dinero_recaudado(self, value):
        self.__dinero_recaudado = value

    @property
    def lista_libros(self):
        return self.__lista_libros

    @lista_libros.setter
    def lista_libros(self, value):
        self.__lista_libros = value

    @property
    def usuarios(self):
        return self.__usuarios

    @usuarios.setter
    def usuarios(self, value):
        self.__usuarios = value

    def __srt__(self):
        texto = (f'Sucursal de {self.__localidad}, {self.__direccion}. Atencion: {self.__horarios_atencion}')
        return texto

    def nuevo_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def nuevo_libro(self, libro):
        self.__lista_libros.append(libro)

    def retirar_libros(self, libro_buscar, usuario_nombre):
        condicion = False
        for libro in self.__lista_libros:
            if libro.nombre == libro_buscar:
                if libro.cantidad_disponible >= 1:
                    condicion = True
                    libro.cantidad_disponible -= libro.cantidad_disponible
                    for usuario in self.__usuarios:
                        if usuario.nombre_usuario == usuario_nombre:
                            usuario.libros_retirados.append(libro)
                            print(
                                f'Libro: {libro.nombre} retirado exitosamente')
                            return print(f'Se ha retirado el libro: {libro}.')
        if condicion == False:
            print(f'(No se cuenta con unidades para realizar el retiro)')
            # usuario con la fecha de devolucion mas proxima
            # lista de usuarios con ese libro
            #lista_usuarios_devolucion = []
            print(f'\n- LISTA DE USUARIOS QUE TIENEN EN ADQUISICION DICHO LIBRO -')
            for usuario in self.__usuarios:
                for libro in usuario.libros_retirados:
                    if libro_buscar == libro.nombre:
                        # lista_usuarios_devolucion.append(usuario)
                        print(f'{usuario.nombre}, {usuario.apellido}')
            # imprimo lista de usuarios que tienen en adquisicion el libro buscado

    def usuarios_por_suscripcion(self):
        print(f'\nLISTA DE USUARIOS POR SUSCRIPCION:')
        print(f'\n-------- SUSCRIPCION PARA ESTUDIANTES --------')
        contador = 1
        for usuario in self.__usuarios:
            if isinstance(usuario.tipo_suscripcion, Suscripcion_alumno) == True:
                print(f'({contador}) {usuario}')
                contador += contador
        contador = 1
        print(f'\n-------- SUSCRIPCION PARA ESTUDIANTES --------')
        for usuario in self.__usuarios:
            if isinstance(usuario.tipo_suscripcion, Suscripcion_estandar) == True:
                print(f'({contador}) {usuario}')




