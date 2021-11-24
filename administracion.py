from os import system
import os, sys
import os
from sucursal import Sucursal

class Administracion():
    def __init__(self):
        self.__lista_sucursales = []
        self.__monto_total_recaudado = None

#GETTER AND SETTER, STR
    @property 
    def lista_sucursales(self):
        return self.__lista_sucursales

    @lista_sucursales.setter
    def lista_sucursales(self,value):
        self.__lista_sucursales = value

    @property
    def monto_total_recaudado(self):
        return self.__monto_total_recaudado

    @monto_total_recaudado.setter
    def monto_total_recaudado(self,value):
        self.__monto_total_recaudado = value

    def __srt__(self):
        texto = 'Gestion de Sucursales de Bibliotecas Populares de la provincia de Misiones!'
        return texto

#METODOS
    def nueva_sucursal(self, localidad, direccion, horarios_atencion):
        sucursal = Sucursal(localidad,direccion,horarios_atencion)
        self.__lista_sucursales.append(sucursal)

    def eliminar_sucursal(self, sucursal):
        self.__lista_sucursales.remove(sucursal)

#LISTA SUCURSALES
    def listado_sucursales(self):
        print(f'--- Lista Sucursales ---')
        contador = 1
        for sucursal_registrada in self.__lista_sucursales:
            print(f'[{contador}] - Sucursal {sucursal_registrada.localidad}')
            contador = contador + 1

#DISTRIBUCION DE LIBROS
    def distribucion_sucursal(self, sucursales_a_buscar, dic_libros_ingreso): #distribucion != stock
        respuesta = 0
        condicional_distribucion = False
        while(condicional_distribucion == False):
            print(f'En que sucursal decia ingresar libros?\n')
            self.lista_sucursales()
            sucursal_elegida = int(input('\nSucursal a eligir: '))
            sucursal_elegida = sucursal_elegida - 1
    
            for key_libro, value_cantidad in dic_libros_ingreso.items():
                ingreso = False
                while(ingreso != True):
                    system("cls")
                    print(f'Cuantos de los [ {value_cantidad} ] libros de {key_libro.nombre} desea ingresa ingresar a la sucursal {self.__lista_sucursales[sucursal_elegida].localidad}?')
                    cantidad_libros = int(input(' '))
                    if cantidad_libros <= value_cantidad:
                        ingreso = True
                        self.__lista_sucursales[sucursal_elegida].nuevo_libro(key_libro,cantidad_libros)
                    else:
                        system("cls")
                        print(f'\nIngrese una cantidad menor o igual a la disponible para distribuir')
                        os.system("pause")
                    system("cls")
                    
            respuesta_YN = 'b'
            while(respuesta_YN != 'Y' and respuesta_YN != 'y' and respuesta_YN != 'N' and respuesta_YN != 'n'):
                system("cls")
                print(f'Desea ingresar libros a otra sucursal? [Y]/[N]')
                respuesta_YN = input(' ')
            if(respuesta_YN == 'N' or respuesta_YN == 'n'):
                condicional_distribucion = True
            #print(f'\nPresione una tecla para continuar . . .')
            os.system("pause")
            system("cls")


        """ for sucursal_buscar in sucursales_a_buscar:
            for sucursal_registrada in self.__lista_sucursales:
                if sucursal_buscar.localidad == sucursal_registrada.localidad and sucursal_buscar.direccion == sucursal_registrada.direccion:
                    for key_libro, value_cantidad in dic_libros_ingreso:
                        pass

                    for libro in dic_libros_ingreso:
                        sucursal_registrada.nuevo_libro(libro) """