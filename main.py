def main():
    from administracion import Administracion
    from sucursal import Sucursal
    from usuario import Usuario
    from libro import Libro
    #from empleado import Empleado
    from suscripcion_alumno import Suscripcion_alumno
    from suscripcion_estandar import Suscripcion_estandar

    suscripcion_alumno = Suscripcion_alumno()
    suscripcion_estandar = Suscripcion_estandar()
    usuario_1 = Usuario('Fabricio Wlodeck','12rwfhg','Fabricio','Wlodeck',20,suscripcion_alumno)
    usuario_2 = Usuario('Santiago Kraiski','gqwerg123','Santiago','Kraiski',20,suscripcion_estandar)
    libro_1 = Libro('Yo Robot', 'Isaac Asimov', '1990', 5, 'ciencia ficcion')
    libro_2 = Libro('El Sol Desnudo', 'Isaac Asimov', '1991', 1, 'ciencia ficcion')
    sucursal_posadas = Sucursal('Posadas','Cordoba 1234','Juan','8am a 10pm',10000)
    administracion = Administracion()
    administracion.nueva_sucursal(sucursal_posadas)

    sucursal_posadas.nuevo_usuario(usuario_1)
    sucursal_posadas.nuevo_usuario(usuario_2)
    sucursal_posadas.nuevo_libro(libro_1)
    sucursal_posadas.nuevo_libro(libro_2)
    sucursal_posadas.retirar_libros(libro_2.nombre,usuario_1.nombre_cuenta)
    sucursal_posadas.retirar_libros(libro_2.nombre,usuario_2.nombre_cuenta)
    
    sucursal_posadas.usuarios_por_suscripcion()
    #usuario_1.listado_libros()
    
if __name__ == '__main__':
    main()