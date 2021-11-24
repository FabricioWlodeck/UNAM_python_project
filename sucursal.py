from usuario import Usuario
from libro import Libro
from suscripcion_alumno import Suscripcion_alumno
from suscripcion_estandar import Suscripcion_estandar
from empleado import Empleado
import datetime


class Sucursal():
    def __init__(self, localidad, direccion, horarios_atencion):
        self.localidad = localidad
        self.__direccion = direccion
        self.__personal = []
        self.__horarios_atencion = horarios_atencion
        self.__dinero_recaudado = 0
        self.__lista_libros = {}  # diccionario de libros donde la clave es otro diccionario con las cantidades disponible, prestadas, retiros en el mes
        self.__usuarios = []  # lista de diccionarios de objetos Usuario

#GETTER AND SETTER, STR
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
        texto = (f'Sucursal de {self.__localidad}, {self.__direccion}. Atencion: {self.__horarios_atencion}')
        return texto

#DINERO_RECAUDADO
    def dinero_recaudado(self):
        print(f'\nDinero recaudado: ${self.__dinero_recaudado}')

#LIBROS
    def nuevo_libro(self,nombre, autor, edicion, genero , cantidad):
        libro = Libro(nombre, autor, edicion, genero)
        existe_previamente = False
        for key_existente, value_existente in self.__lista_libros.items():
                if libro == key_existente:
                    existe_previamente = True
                    for key_cantidades, value_cantidades in value_existente.items(): 
                        if key_cantidades == 'cantidades_disponibles':
                            value_cantidades = value_cantidades + cantidad
                        pass
                    value_existente = value_existente + cantidad
        if existe_previamente == False:
            self.__lista_libros[libro] = {'cantidades_disponibles': cantidad, 'cantidades_prestadas': 0}

            #self.__lista_libros[libro] = cantidad

    def eliminar_libro(self, libro):
        self.__lista_libros.remove(libro)

    def retirar_libro(self, lista_libros_retirar, usuario_nombre,usuario_apellido):
        condicion = False
        for libro_a_retirar in lista_libros_retirar:
            for libro in self.__lista_libros:
                if libro_a_retirar.nombre == libro.nombre:
                    if libro.cantidad_disponible >= 1:
                        condicion = True
                        libro.cantidad_disponible = libro.cantidad_disponible - 1
                        libro.unidades_prestadas = libro.unidades_prestadas + 1
                        for usuario in self.__usuarios:
                            if usuario.nombre == usuario_nombre:
                                if usuario.apellido == usuario_apellido:
                                    usuario.libros_retirados.append(libro)
                                    fecha_actual = datetime.date.today()
                                    if libro.tipo == 'academico':
                                        margen_dias = datetime.timedelta(days=14)
                                    else:
                                        margen_dias = datetime.timedelta(days=28)

                                    margen_dias = datetime.timedelta(days=-1)
                                    
                                    libro.fecha_devolucion = fecha_actual + margen_dias
                                    print(f'Se ha retirado el libro: {libro}. Fecha de devolucion: {libro.fecha_devolucion} [{margen_dias.days} dias]')
                                    print(
                                        f'Libro: {libro.nombre} retirado exitosamente')
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
                    if lista_libros_retirar == libro.nombre:
                        # lista_usuarios_devolucion.append(usuario)
                        print(
                            f'({contador}) {usuario.nombre}, {usuario.apellido}')
                        contador += contador
            # imprimo lista de usuarios que tienen en adquisicion el libro buscado

    def devolver_libro(self, lista_libros_devolver,usuario_nombre):
        contador = 1
        for usuario in self.__usuarios:
            if usuario.nombre_cuenta == usuario_nombre: #DA PROBLEMAAAAAAAAAASSSSSSSSSSSSSSS!!!!!!!!!!
                usuario.listado_libros_usuario()
                for libro_en_devolucion in lista_libros_devolver:
                    for libro_retirado in usuario.libros_retirados:
                        if libro_retirado.nombre == libro_en_devolucion.nombre:
                            usuario.libros_retirados.remove(libro_retirado)
                            for libro_a_devolver in self.__lista_libros:
                                if libro_a_devolver.nombre == libro_en_devolucion.nombre:
                                    fecha_actual = datetime.date.today()
                                    dias_de_retraso = (libro_a_devolver.fecha_devolucion - fecha_actual)
                                    if dias_de_retraso.days < 0:
                                        print(f'\ndias de retraso: {-1*dias_de_retraso.days}')
                                        monto_por_atraso = (-1*dias_de_retraso.days) * libro_a_devolver.interes_atraso
                                        self.__dinero_recaudado = self.__dinero_recaudado + monto_por_atraso 
                                        print(f'Monto por atraso: ${monto_por_atraso}')
                                    else:
                                        print(f'\nDias de retraso: 0\nDias para devolucion: {dias_de_retraso.days}')
                                    #print(f'\nlibros de {usuario}: {usuario.libros_retirado}')
                                    libro_a_devolver.cantidad_disponible = libro_a_devolver.cantidad_disponible + 1
                                    libro_a_devolver.unidades_prestadas = libro_a_devolver.unidades_prestadas - 1
                                    #print(f'\nLibro: [{libro_en_devolucion}]\nLibro en busqueda: [{libro_retirado.nombre}]')
                                    print(f'\n\tLibro: [{libro_retirado.nombre}] devuelto exitosamente')
                        contador = contador + 1


    def listado_libros(self):
        #voy mostrando el libro con sus repestivas cantidades, las cuales estan almacenadas en un diccionario dentro del atributo valor del diccionario general que almacena los libros
        contador = 0
        for key_existente, value_existente in self.__lista_libros.items():
            for key_cantidad, value_cantidad in value_existente.items():
                contador = contador + value_cantidad

        print(f'----- LISTA DE LIBROS EN SUCURSAL {self.__localidad} [{contador} unidades] -----')
        #for libros in self.__lista_libros:
        cantidad_disponible = 0
        cantidad_prestada = 0
        for key_existente, value_existente in self.__lista_libros.items():
            for key_cantidad, value_cantidad in value_existente.items():
                if key_cantidad == 'cantidades_disponibles':
                    cantidad_disponible = value_cantidad
                else:
                    cantidad_prestada = value_cantidad
            print(f'{key_existente}\nunidades: {cantidad_disponible}\nUnidades prestadas: {cantidad_prestada}\n')

    def libro_mas_retirado(self):
        cantidad_prestada = 0
        libro_mas_retirado = None
        for key_existente, value_existente in self.__lista_libros.items():
            for key_cantidad, value_cantidad in value_existente.items():
                if key_cantidad == 'cantidades_prestadas':
                    if value_cantidad > cantidad_prestada:
                        libro_mas_retirado = key_existente
                        cantidad_prestada = value_cantidad
        print(f'* {self.__localidad}: {libro_mas_retirado} con {cantidad_prestada} retiros')

# USUARIOS
    def nuevo_usuario(self, nombre, apellido, edad, tipo_suscripcion):
        usuario =Usuario(nombre, apellido, edad, tipo_suscripcion)
        self.__dinero_recaudado =  self.__dinero_recaudado + tipo_suscripcion.costo_suscripcion
        self.__usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self.__usuarios.remove(usuario)

    def usuarios_por_suscripcion(self):
        print(f'\nLISTA DE USUARIOS POR SUSCRIPCION:')
        contador = 0
        for usuario in self.__usuarios:
            texto_libros = ''
            for libros in usuario.libros_retirados:
                texto_libros = texto_libros +' - '+ str(libros)

            if usuario.tipo_suscripcion.tipo == 'Estudiante':
                contador = contador + 1

        print(f'\n---------- SUSCRIPCION ESTUDIANTE: [{contador}] ----------')
        contador = 1
        for usuario in self.__usuarios:
            if usuario.tipo_suscripcion.tipo == 'Estudiante':
                print(f'({contador}) {usuario}\nLibros retirados[{texto_libros}]\n')
                contador = contador + 1
        # ---------------------- ESTANDAR -----------------------

        contador = 0
        for usuario in self.__usuarios:
            texto_libros = ''
            for libros in usuario.libros_retirados:
                texto_libros = texto_libros + str(libros)
            if isinstance(usuario.tipo_suscripcion, Suscripcion_estandar) == True:
                contador = contador + 1

        print(f'\n---------- SUSCRIPCION ESTANDAR:   [{contador}] ----------')
        contador = 1
        for usuario in self.__usuarios:
            if usuario.tipo_suscripcion.tipo == 'Estandar':
                print(f'({contador}) {usuario}\nLibros retirados[{texto_libros}]\n')
                contador = contador + 1

# EMPLEADOS
    def nuevo_empleado(self, nombre, apellido, edad, horas, cargo, sueldo):
        empleado = Empleado(nombre, apellido, edad, horas, cargo, sueldo)
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

   