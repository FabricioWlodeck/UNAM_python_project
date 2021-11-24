from os import system
import os, sys
import os
from administracion import Administracion
from sucursal import Sucursal
from usuario import Usuario
from libro import Libro
from empleado import Empleado
from suscripcion import Suscripcion

from suscripcion_alumno import Suscripcion_alumno
from suscripcion_estandar import Suscripcion_estandar
import datetime

def main():

#------------ INSTANCIAS DE OBJETOS ------------
    fecha_actual = datetime.date.today()
    margen_caducidad_suscripcion = datetime.timedelta(days=365)
    fecha_caducidad = fecha_actual + margen_caducidad_suscripcion
    suscripcion_alumno = Suscripcion(500,margen_caducidad_suscripcion,5,fecha_actual,fecha_caducidad)
    suscripcion_estandar = Suscripcion(750,margen_caducidad_suscripcion,7,fecha_actual,fecha_caducidad)

    empleado_1 = Empleado('Raul','Perez',35,'7am a 13pm','Gerente',55000)
    empleado_2 = Empleado('Juan','Antunez',35,'7am a 13pm','Caja',38000)

    #INSTANCIAR USUARIO DIRECMENTE EN LA SUCURSAL
    usuario_1 = Usuario('Fabricio','Wlodeck',20,suscripcion_alumno)
    usuario_2 = Usuario('Santiago','Kraiski',20,suscripcion_estandar)

    libro_1 = Libro('Yo Robot', 'Isaac Asimov', '1990', 'ciencia ficcion')
    libro_2 = Libro('El Sol Desnudo', 'Isaac Asimov', '1991', 'ciencia ficcion')
    libro_3 = Libro('Cool Boot Attack', 'Alex Halderman∗,', '2008',  'academico')

    sucursal_posadas = Sucursal('Posadas','Cordoba 1234','8am a 10pm')
    administracion = Administracion()

#------------ SUSCRIPCION / STOCK / ALMACENAMIENTO  DE LAS OBJETOS INSTANCIADOS ------------
    administracion.nueva_sucursal(sucursal_posadas)

    sucursal_posadas.nuevo_usuario(usuario_1)
    sucursal_posadas.nuevo_usuario(usuario_2)

    sucursal_posadas.nuevo_empleado(empleado_1)
    sucursal_posadas.nuevo_empleado(empleado_2)

    #INGRESO/RESTOCK MEDIANTE ADMINISTRACION
    administracion.distribucion_sucursal([sucursal_posadas],{libro_1:2,libro_2:2})
    """ sucursal_posadas.nuevo_libro(libro_1)
    sucursal_posadas.nuevo_libro(libro_2)
    sucursal_posadas.nuevo_libro(libro_3) """
    
    sucursal_posadas.usuarios_por_suscripcion()
    sucursal_posadas.empleados_sucursal()

    sucursal_posadas.listado_libros()
    #RETIRO/PRESTAMO DE LISTA DE LIBROS A UN USUARIO REGISTRADO
    sucursal_posadas.retirar_libro([libro_2],usuario_1.nombre, usuario_1.apellido)
    sucursal_posadas.retirar_libro([libro_2],usuario_1.nombre, usuario_1.apellido)

    sucursal_posadas.listado_libros()
    """ sucursal_posadas.eliminar_libro(libro_1)
    sucursal_posadas.listado_libros()
    sucursal_posadas.eliminar_usuario(usuario_1)
    sucursal_posadas.usuarios_por_suscripcion()
    sucursal_posadas.eliminar_empleado(empleado_1)
    sucursal_posadas.empleados_sucursal() """
    sucursal_posadas.dinero_recaudado()

    sucursal_posadas.devolver_libro([libro_1],usuario_1.nombre)
    sucursal_posadas.listado_libros()

    sucursal_posadas.nuevo_libro(libro_1)
    sucursal_posadas.listado_libros()

    #usuario_1.listado_libros()

def interfaz_general():
    system("cls")
    print(f'\n--------- Sistema de Bibliotecas Publicas de Misiones ---------')
    print(f'\n---------           Opciones del Sistema       ---------\n')
    print(f'[1]- Mostrar Datos')
    print(f'[2]- Cargar Datos')
    print(f'[3]- Eliminar Datos')
    print(f'[4]- Salir')

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
    
def main2():
    administracion = Administracion()
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
                administracion.lista_sucursales()

            if(opcion_mostrar == 2):
                pass

            if(opcion_mostrar == 3):
                pass

            if(opcion_mostrar== 4):
                pass

            if(opcion_mostrar == 5):
                pass

        if(opcion == 2):
            interfaz_datos()
            opcion_mostrar = 0
            while(opcion_mostrar != 1 and opcion_mostrar != 2 and opcion_mostrar != 3 and opcion_mostrar != 4):
                opcion_mostrar = int(input('\nIngrese una opcion entre las dadas: '))
            if(opcion_mostrar == 1):
                localidad = input('\nIngrese la localidad: ')
                direccion = input('\nIngrese una direccion: ')
                horario = input('\nIngrese el horario de atencion (como string): ')
                administracion.nueva_sucursal(localidad,direccion,horario)

            if(opcion_mostrar == 2):
                pass

            if(opcion_mostrar == 3):
                pass

            if(opcion_mostrar== 4):
                pass

            if(opcion_mostrar == 5):
                pass
            system("cls")
            pass

        if(opcion == 3):
            system("cls")
            pass

        if(opcion == 4):
            system("cls")
            pass
        os.system("pause")
        opcion = 0
if __name__ == '__main__':
    main2()
    #main()