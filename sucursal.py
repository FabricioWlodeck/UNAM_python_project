from usuario import Usuario
from libro import Libro
from suscripcion_alumno import Suscripcion_alumno
from suscripcion_estandar import Suscripcion_estandar
import datetime


class Sucursal():
    def __init__(self, localidad, direccion, horarios_atencion):
        self.localidad = localidad
        self.__direccion = direccion
        self.__personal = []
        self.__horarios_atencion = horarios_atencion
        self.__dinero_recaudado = 0
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
        texto = (
            f'Sucursal de {self.__localidad}, {self.__direccion}. Atencion: {self.__horarios_atencion}')
        return texto

#DINERO_RECAUDADO
    def dinero_recaudado(self):
        print(f'\nDinero recaudado: ${self.__dinero_recaudado}')

# LIBROS

    def nuevo_libro(self, libro):
        self.__lista_libros.append(libro)

    def eliminar_libro(self, libro):
        self.__lista_libros.remove(libro)

    def retirar_libro(self, libro_buscar, usuario_nombre):
        condicion = False
        for libro in self.__lista_libros:
            if libro.nombre == libro_buscar:
                if libro.cantidad_disponible >= 1:
                    condicion = True
                    libro.cantidad_disponible -= libro.cantidad_disponible
                    libro.unidades_prestadas = libro.unidades_prestadas + 1
                    for usuario in self.__usuarios:
                        if usuario.nombre_cuenta == usuario_nombre:
                            usuario.libros_retirados.append(libro)
                            fecha_actual = datetime.date.today()
                            if libro.tipo == 'academico':
                                margen_dias = datetime.timedelta(days=14)
                            else:
                                margen_dias = datetime.timedelta(days=28)
                            libro.fecha_devolucion = fecha_actual + margen_dias
                            print(f'Se tendra que devolver dentro de {libro.fecha_devolucion}')
                            print(
                                f'Libro: {libro.nombre} retirado exitosamente')
                            return print(f'Se ha retirado el libro: {libro}.')
        if condicion == False:
            print(f'(No se cuenta con unidades para realizar el retiro)')
            # usuario con la fecha de devolucion mas proxima
            # lista de usuarios con ese libro
            #lista_usuarios_devolucion = []
            print(
                f'\n------ LISTA DE USUARIOS QUE TIENEN EN ADQUISICION DICHO LIBRO ------')
            contador = 1
            for usuario in self.__usuarios:
                for libro in usuario.libros_retirados:
                    if libro_buscar == libro.nombre:
                        # lista_usuarios_devolucion.append(usuario)
                        print(
                            f'({contador}) {usuario.nombre}, {usuario.apellido}')
                        contador += contador
            # imprimo lista de usuarios que tienen en adquisicion el libro buscado

    def devolver_libro(self, libro_en_devolucion,usuario_nombre):
        contador = 1
        for usuario in self.__usuarios:
            #print(f'\n\tUsuario: {usuario.nombre_cuenta}\n\tLibro buscado: {libro_en_devolucion}')
            #print(f'\n\t{usuario_nombre}')
            if usuario.nombre_cuenta == usuario_nombre: #DA PROBLEMAAAAAAAAAASSSSSSSSSSSSSSS!!!!!!!!!!

                #print(f'\n\tUsuario: {usuario.nombre_cuenta}\n\tLibro buscado: {libro_en_devolucion}')
                for libro_retirado in usuario.libros_retirados:
                    print(f'\n{contador} HOLAAA CONFIRMO!! {usuario.libros_retirados[0]}')
                    if libro_retirado.nombre == libro_en_devolucion:
                        usuario.libros_retirados.remove(libro_retirado)
                        for libro_a_devolver in self.__lista_libros:
                            if libro_a_devolver.nombre == libro_en_devolucion:
                                print(f'libros {usuario}: {usuario.libros_retirados}')
                                libro_a_devolver.cantidad_disponible = libro_a_devolver.cantidad_disponible + 1
                                libro_a_devolver.unidades_prestadas = libro_a_devolver.unidades_prestadas - 1
                    contador = contador + 1


    def listado_libros(self):
        contador = 0
        for libros in self.__lista_libros:
            contador = libros.cantidad_disponible + libros.unidades_prestadas + contador

        print(
            f'\n----- LISTA DE LIBROS EN SUCURSAL {self.__localidad} [{contador} unidades] -----')
        for libros in self.__lista_libros:
            print(
                f'{libros}\nunidades: {libros.cantidad_disponible}\nUnidades prestadas: {libros.unidades_prestadas}\n')

# USUARIOS
    def nuevo_usuario(self, usuario):

        self.__dinero_recaudado =  self.__dinero_recaudado + usuario.tipo_suscripcion.costo_suscripcion
        self.__usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self.__usuarios.remove(usuario)

    def usuarios_por_suscripcion(self):
        print(f'\nLISTA DE USUARIOS POR SUSCRIPCION:')
        contador = 0
        for usuario in self.__usuarios:
            if isinstance(usuario.tipo_suscripcion, Suscripcion_alumno) == True:
                contador = contador + 1

        print(f'\n---------- SUSCRIPCION ESTUDIANTE: [{contador}] ----------')
        contador = 1
        for usuario in self.__usuarios:
            if isinstance(usuario.tipo_suscripcion, Suscripcion_alumno) == True:
                print(f'({contador}) {usuario}\n')
                contador = contador + 1
        # ---------------------- ESTANDAR -----------------------

        contador = 0
        for usuario in self.__usuarios:
            if isinstance(usuario.tipo_suscripcion, Suscripcion_estandar) == True:
                contador = contador + 1

        print(f'\n---------- SUSCRIPCION ESTANDAR: [{contador}] ----------')
        contador = 1
        for usuario in self.__usuarios:
            if isinstance(usuario.tipo_suscripcion, Suscripcion_estandar) == True:
                print(f'({contador}) {usuario}\n')
                contador = contador + 1

# EMPLEADOS
    def nuevo_empleado(self, empleado):
        self.__personal.append(empleado)

    def eliminar_empleado(self, empleado):
        self.__personal.remove(empleado)

    def empleados_sucursal(self):

        contador = 0
        for empleado in self.__personal:
            contador = contador + 1
        print(f'\n---------- LISTA DE EMPLEADOS [{contador}]----------')
        for empleado in self.__personal:
            print(f'{empleado}\n')
            contador = contador + 1
