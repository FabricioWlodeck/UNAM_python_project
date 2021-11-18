class Administracion():
    def __init__(self):
        self.__lista_sucursales = []
        self.__monto_total_recaudado = None

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

    def nueva_sucursal(self, sucursal):
        self.__lista_sucursales.append(sucursal)

    def eliminar_sucursal(self, sucursal):
        self.__lista_sucursales.remove(sucursal)

    def stock_sucursal(self, sucursales_a_buscar,libros_ingreso):
        for sucursal_buscar in sucursales_a_buscar:
            for sucursal_registrada in self.__lista_sucursales:
                if sucursal_buscar.localidad == sucursal_registrada.localidad and sucursal_buscar.direccion == sucursal_registrada.direccion:
                    for libro in libros_ingreso:
                        sucursal_registrada.nuevo_libro(libro)