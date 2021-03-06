from os import system
import os, sys
import sys
import os
from administracion import Administracion
from sucursal import Sucursal
from usuario import Usuario
from libro import Libro
from empleado import Empleado
from suscripcion import Suscripcion

import datetime

def interfaz_general():
    system("cls")
    print(f'\n--------- Sistema de Bibliotecas Publicas de Misiones ---------')
    print(f'\n---------           Opciones del Sistema       ---------\n')
    print(f'[1]- Mostrar Datos')
    print(f'[2]- Cargar Datos')
    print(f'[3]- Eliminar Datos')
    print(f'[4]- Retirar/Devolver libro')
    print(f'[5]- Salir')

def interfaz_mostrar():
    system("cls")
    print(f'\n--------- Sistema de Bibliotecas Publicas de Misiones ---------')
    print(f'\n---------           Opciones del Sistema       ---------\n')
    print(f'[1]- Lista de Sucursales en la Provincia')
    print(f'[2]- Lista de libros por Sucursal')
    print(f'[3]- Lista de Usuarios por Sucursal')
    print(f'[4]- Lista de Empleados por Sucursal')
    print(f'[5]- Lista de libros mas retirados por Sucursal')

def interfaz_datos():
    system("cls")
    print(f'\n--------- Sistema de Bibliotecas Publicas de Misiones ---------')
    print(f'\n---------           Opciones del Sistema       ---------\n')
    print(f'[1]- Ingresar nueva Sucursal')
    print(f'[2]- Ingresar nuevos Libros')
    print(f'[3]- Ingresar nuevos Empleados')
    print(f'[4]- Ingresar nuevos Usuarios')
    
def interfaz_eliminacion():
    system("cls")
    print(f'\n--------- Sistema de Bibliotecas Publicas de Misiones ---------')
    print(f'\n---------           Opciones del Sistema       ---------\n')
    print(f'[1]- Eliminar Sucursal')
    print(f'[2]- Eliminar Libros')
    print(f'[3]- Eliminar Empleados')
    print(f'[4]- Eliminar Usuarios')

def interfaz_retiro_devolucion():
    system("cls")
    print(f'\n--------- Sistema de Bibliotecas Publicas de Misiones ---------')
    print(f'\n---------           Opciones del Sistema       ---------\n')
    print(f'[1]- Retirar Libro')
    print(f'[2]- Devolver Libro')


def main():
    administracion = Administracion()
    administracion.nueva_sucursal('Posadas','Cordoba 1234','8am a 10pm')
    fecha_actual = datetime.date.today()
    margen_caducidad_suscripcion = datetime.timedelta(days=365)
    fecha_caducidad = fecha_actual + margen_caducidad_suscripcion

    suscripcion_alumno = Suscripcion(500,margen_caducidad_suscripcion,5,fecha_actual,fecha_caducidad,'Estudiante')
    suscripcion_estandar = Suscripcion(750,margen_caducidad_suscripcion,7,fecha_actual,fecha_caducidad,'Estandar')

    administracion.lista_sucursales[0].nuevo_libro('Yo Robot', 'Isaac Asimov', '1990', 'Ciencia Ficcion' , 5)
    administracion.lista_sucursales[0].nuevo_libro('El Sol Desnudo', 'Isaac Asimov', '1970', 'Ciencia Ficcion' , 1)     #
    administracion.lista_sucursales[0].nuevo_empleado('Mateo', 'Amarilla', 20, 8, 'Repositor', 50000)

    administracion.lista_sucursales[0].nuevo_usuario('Fabricio', 'Wlodeck', 20, suscripcion_alumno)                          #
    administracion.lista_sucursales[0].nuevo_usuario('Juani', 'Lopez', 20, suscripcion_estandar)
    administracion.lista_sucursales[0].nuevo_usuario('Sebastian', 'Monzon', 20, suscripcion_alumno)

    #Estructura de guardado de libros dentro de una sucursal
    """ {
        libro_1 : {'cantidades_disponibles':0, 'cantidades_prestadas': 0}, libro_2 : {'cantidades_disponibles':0, 'cantidades_prestadas':0}
    } """



    opcion = 0
    while(opcion != 4):
        interfaz_general()
        #os.system("pause")
        while(opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4):
            opcion = int(input('\nIngrese una opcion entre las dadas: '))

        if(opcion == 1):
            system("cls")
            interfaz_mostrar()
            opcion = 0
            opcion_mostrar = 0
            while(opcion_mostrar != 1 and opcion_mostrar != 2 and opcion_mostrar != 3 and opcion_mostrar != 4 and opcion_mostrar != 5):
                opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))

            if(opcion_mostrar == 1):
                system("cls")
                administracion.listado_sucursales()
                print(f'\n')

            if(opcion_mostrar == 2):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal para listar sus libros')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                administracion.lista_sucursales[opcion_mostrar].listado_libros()

            if(opcion_mostrar == 3):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal para listar sus libros')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                administracion.lista_sucursales[opcion_mostrar].usuarios_por_suscripcion()

            if(opcion_mostrar== 4):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal para listar sus libros')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                administracion.lista_sucursales[opcion_mostrar].empleados_sucursal()

            if(opcion_mostrar == 5):
                system("cls")
                print(f'\n----- LISTA DE LIBROS MAS RETIRADOS POR SUCURSAL -----\n')
                for sucursal in administracion.lista_sucursales:
                    sucursal.libro_mas_retirado()
                print(f'\n')

        if(opcion == 2):
            interfaz_datos()
            opcion_mostrar = 0
            while(opcion_mostrar != 1 and opcion_mostrar != 2 and opcion_mostrar != 3 and opcion_mostrar != 4 and opcion_mostrar != 5):
                opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
            if(opcion_mostrar == 1):
                system("cls")
                print(f'-------- Ingrese los datos de la Sucursal a registrar --------')
                localidad = input('\nIngrese la localidad: ')
                direccion = input('\nIngrese una direccion: ')
                horario = input('\nIngrese el horario de atencion (como string): ')
                administracion.nueva_sucursal(localidad,direccion,horario)

            if(opcion_mostrar == 2):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal para listar sus libros')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                print(f'-------- Ingrese los datos del Libro a registrar --------')
                nombre = input('\nIngrese el nombre del libro: ')
                autor = input('\nIngrese el autor del libro: ')
                edicion = input('\nIngrese el edicion del libro (anio): ')
                genero = input('\nIngrese el genero del libro: ')
                cantidad = int(input('\nIngrese el numero de unidades del libro: '))
                administracion.lista_sucursales[opcion_mostrar].nuevo_libro(nombre, autor, edicion, genero , cantidad)

            if(opcion_mostrar == 3):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal a la cual se le cargara el Empleado')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                print(f'-------- Ingrese los datos del Empleado a registrar --------')
                nombre = input('\nIngrese el nombre del Empleado: ')
                apellido = input('\nIngrese el apellido del Empleado: ')
                edad = int(input('\nIngrese la edad del empleado: '))
                horas = int(input('\nIngrese las cantidad de horas de un turno diario: '))
                cargo = input('\nIngrese el cargo del Empleado: ')
                sueldo = int(input('\nIngrese el Sueldo del Empleado: '))
                
                #empleado_1 = Empleado('Raul','Perez',35,'7am a 13pm','Gerente',55000)
                administracion.lista_sucursales[opcion_mostrar].nuevo_empleado( nombre, apellido, edad, horas, cargo, sueldo)

            if(opcion_mostrar== 4):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal a la cual se le cargara el Usuario')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                print(f'-------- Ingrese los datos del Usuario a registrar --------')
                nombre = input('\nIngrese el nombre del Usuario: ')
                apellido = input('\nIngrese el apellido del Usuario: ')
                edad = int(input('\nIngrese la edad del Usuario: '))

                respuesta = 'O'
                tipo_suscripcion = None

                while respuesta != 'E' and respuesta != 'e' and respuesta != 'S' and respuesta != 's':
                    respuesta = input('\nSeleccione [E] para suscripcion de Estudiante y [S] para suscripcion Estandar: ')
                    system("cls")

                if respuesta == 'e' or respuesta == 'E':
                    tipo_suscripcion = suscripcion_alumno
                    print('\nSuscripcion Estudiante')
                else:
                    tipo_suscripcion = suscripcion_estandar
                    print('\nSuscripcion Estandar')
                #empleado_1 = Empleado('Raul','Perez',35,'7am a 13pm','Gerente',55000)
                administracion.lista_sucursales[opcion_mostrar].nuevo_usuario( nombre, apellido, edad, tipo_suscripcion)

            system("cls")
            pass

        if(opcion == 3):
            interfaz_eliminacion()
            contador = 0
            for sucu in administracion.lista_sucursales:
                contador = contador + 1
            opcion_mostrar = 0
            while(opcion_mostrar != 1 and opcion_mostrar != 2 and opcion_mostrar != 3 and opcion_mostrar != 4):
                opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))

            if(opcion_mostrar == 1):
                system("cls")
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal a Eliminar')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                administracion.eliminar_sucursal(administracion.lista_sucursales[opcion_mostrar])
            
            if(opcion_mostrar == 2):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal en la cual se Eliminaran los Libro:\n')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                
                libros_por_titulo = 0
                for key in administracion.lista_sucursales[opcion_mostrar].lista_libros:
                    libros_por_titulo = libros_por_titulo + 1

                opcion_eliminar = 0
                while(opcion_eliminar < 1 or opcion_eliminar > libros_por_titulo):
                    print(f'---------- Seleccione un Libro a Eliminar ----------\n')
                    administracion.lista_sucursales[opcion_mostrar].listado_libros()
                    opcion_eliminar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_eliminar = opcion_eliminar - 1

                libro_a_eliminar = None
                contador = 0
                for key in administracion.lista_sucursales[opcion_mostrar].lista_libros:
                    if contador == opcion_eliminar:
                        libro_a_eliminar = key
                    contador = contador + 1
                
                administracion.lista_sucursales[opcion_mostrar].eliminar_libro(libro_a_eliminar)

            if(opcion_mostrar == 3):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal en la cual se Eliminaran los Empleados:\n')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                
                cant_empleados = 0
                for emple in administracion.lista_sucursales[opcion_mostrar].personal:
                    cant_empleados = cant_empleados + 1

                opcion_eliminar = 0
                while(opcion_eliminar < 1 or opcion_eliminar > cant_empleados):
                    print(f'---------- Seleccione un Empleado a Eliminar ----------')
                    administracion.lista_sucursales[opcion_mostrar].empleados_sucursal()
                    opcion_eliminar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_eliminar = opcion_eliminar - 1

                empleado_a_eliminar = None
                contador = 0
                for emple in administracion.lista_sucursales[opcion_mostrar].personal:
                    if contador == opcion_eliminar:
                        empleado_a_eliminar = emple
                    contador = contador + 1
                
                administracion.lista_sucursales[opcion_mostrar].eliminar_empleado(empleado_a_eliminar)

            if(opcion_mostrar == 4):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal en la cual se Eliminaran los Usuarios:\n')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_mostrar = opcion_mostrar - 1
                system("cls")
                
                cant_usuarios = 0
                for usu in administracion.lista_sucursales[opcion_mostrar].usuarios:
                    cant_usuarios = cant_usuarios + 1

                opcion_eliminar = 0
                while(opcion_eliminar < 1 or opcion_eliminar > cant_usuarios):
                    print(f'---------- Seleccione un Empleado a Eliminar ----------')
                    administracion.lista_sucursales[opcion_mostrar].usuarios_por_suscripcion()
                    opcion_eliminar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                opcion_eliminar = opcion_eliminar - 1

                usuario_a_eliminar = None
                contador = 0
                for usu in administracion.lista_sucursales[opcion_mostrar].usuarios:
                    if contador == opcion_eliminar:
                        usuario_a_eliminar = usu
                    contador = contador + 1
                
                administracion.lista_sucursales[opcion_mostrar].eliminar_usuario(usuario_a_eliminar)

        if(opcion == 4):
            interfaz_retiro_devolucion()
            contador = 0
            opcion_mostrar = 0
            while(opcion_mostrar < 1 or opcion_mostrar > 2):
                opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                system("cls")
            system("cls")

            #seleccionar Sucursal aunque se deberia validar/buscar el usuario en todas las sucursales tal vez

            if(opcion_mostrar == 1):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal para Retirar su libro')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                #DATO SUCURSAL ELEGIDA    
                opcion_mostrar = opcion_mostrar - 1
                system("cls")

                usuario_a_retirar = None
                usuario_registrado = False
                print(f'-------- Ingrese Su Nombre y Apellido (como Figura en su Registro) --------')
                nombre = input('\nIngrese su nombre de Usuario: ')
                apellido = input('\nIngrese su apellido de Usuario: ')
                for usuario in administracion.lista_sucursales[opcion_mostrar].usuarios:
                    if usuario.apellido == apellido and usuario.nombre == nombre:
                        usuario_registrado = True
                        usuario_a_retirar = usuario

                if usuario_registrado == True:
                    system("cls")
                    libros_por_titulo = 0
                    for key in administracion.lista_sucursales[opcion_mostrar].lista_libros:
                        libros_por_titulo = libros_por_titulo + 1

                    opcion_retirar = 0
                    while(opcion_retirar < 1 or opcion_retirar > libros_por_titulo):
                        print(f'---------- Seleccione un Libro a Retirar ----------\n')
                        administracion.lista_sucursales[opcion_mostrar].listado_libros()
                        opcion_retirar = int(input('\nIngrese una opcion entre las dadas: '))
                        system("cls")
                    opcion_retirar = opcion_retirar - 1

                    orden_libro_retirar = 0
                    libro_retirar=None
                    for key in administracion.lista_sucursales[opcion_mostrar].lista_libros:
                        if orden_libro_retirar == opcion_retirar:
                            libro_retirar = key
                        orden_libro_retirar = orden_libro_retirar + 1

                    administracion.lista_sucursales[opcion_mostrar].retirar_libro(libro_retirar,usuario_a_retirar)

                else:
                    system("cls")
                    print(f'El Usuario Ingresado no se encuentra Registrado en esta Sucursal, por ende no puede realizar retiros')

                
            if(opcion_mostrar == 2):
                system("cls")
                contador = 0
                for sucu in administracion.lista_sucursales:
                    contador = contador + 1
                opcion_mostrar = 0
                while(opcion_mostrar < 1 or opcion_mostrar > contador):
                    print(f'Seleccione una Sucursal para Devolver su libro')
                    administracion.listado_sucursales()
                    opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
                    system("cls")
                #DATO SUCURSAL ELEGIDA    
                opcion_mostrar = opcion_mostrar - 1
                system("cls")

                usuario_a_retirar = None
                usuario_registrado = False
                iterador = 0
                posicion_usuario_en_lista = 0
                print(f'-------- Ingrese Su Nombre y Apellido (como Figura en su Registro) --------')
                nombre = input('\nIngrese su nombre de Usuario: ')
                apellido = input('\nIngrese su apellido de Usuario: ')
                for usuario in administracion.lista_sucursales[opcion_mostrar].usuarios:
                    if usuario.apellido == apellido and usuario.nombre == nombre:
                        usuario_registrado = True
                        usuario_a_retirar = usuario
                    else:
                        iterador = iterador + 1

                if usuario_registrado == True:
                    system("cls")
                    libros_por_titulo = 0
                    #TENGO QUE FIJARME EN LA LISTA DE RETIRO DEL USUARIO, NO EN LA LISTA DE LIBROS DE LA SUCURSAL
                    for libro in administracion.lista_sucursales[opcion_mostrar].usuarios[posicion_usuario_en_lista].libros_retirados:
                        libros_por_titulo = libros_por_titulo + 1

                    opcion_retirar = 0
                    while(opcion_retirar < 1 or opcion_retirar > libros_por_titulo):
                        print(f'---------- Seleccione un Libro a Devolver ----------')
                        administracion.lista_sucursales[opcion_mostrar].usuarios[posicion_usuario_en_lista].retornar_lista_libros_formato_menu()
                        opcion_retirar = int(input('\nIngrese una opcion entre las dadas: '))
                        system("cls")
                    opcion_retirar = opcion_retirar - 1

                    administracion.lista_sucursales[opcion_mostrar].devolver_libro(libro_retirar,usuario_a_retirar)

                else:
                    system("cls")
                    print(f'El Usuario Ingresado no se encuentra Registrado en esta Sucursal, por ende no se puede devolver su libro')

        if(opcion == 5):
            system("cls")
            sys.exit()
        
        os.system("pause")
        opcion = 0
if __name__ == '__main__':
    main()
    #main()