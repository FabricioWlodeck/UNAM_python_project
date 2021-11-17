def main():
    from administracion import Administracion
    from sucursal import Sucursal
    from usuario import Usuario
    from libro import Libro
    from empleado import Empleado
    from suscripcion_alumno import Suscripcion_alumno
    from suscripcion_estandar import Suscripcion_estandar

    suscripcion_alumno = Suscripcion_alumno()
    suscripcion_estandar = Suscripcion_estandar()
    empleado_1 = Empleado('Raul Perez','fe2fv~1!','Raul','Perez',35,'7am a 13pm','Gerente',55000)
    empleado_2 = Empleado('Juan Felipe','fe2fv~1!','Juan','Antunez',35,'7am a 13pm','Caja',38000)

    usuario_1 = Usuario('Fabricio Wlodeck','12rwfhg','Fabricio','Wlodeck',20,suscripcion_alumno)
    usuario_2 = Usuario('Santiago Kraiski','gqwerg123','Santiago','Kraiski',20,suscripcion_estandar)
    libro_1 = Libro('Yo Robot', 'Isaac Asimov', '1990', 5, 'ciencia ficcion')
    libro_2 = Libro('El Sol Desnudo', 'Isaac Asimov', '1991', 1, 'ciencia ficcion')
    libro_3 = Libro('Cool Boot Attack', 'Alex Halderman∗,', '2008', 1, 'academico')
    sucursal_posadas = Sucursal('Posadas','Cordoba 1234','8am a 10pm')
    administracion = Administracion()
    administracion.nueva_sucursal(sucursal_posadas)

    sucursal_posadas.nuevo_usuario(usuario_1)
    sucursal_posadas.nuevo_usuario(usuario_2)

    sucursal_posadas.nuevo_empleado(empleado_1)
    sucursal_posadas.nuevo_empleado(empleado_2)

    sucursal_posadas.nuevo_libro(libro_1)
    sucursal_posadas.nuevo_libro(libro_2)
    sucursal_posadas.nuevo_libro(libro_3)
    
    sucursal_posadas.retirar_libro(libro_2.nombre,usuario_1.nombre_cuenta)
    sucursal_posadas.retirar_libro(libro_2.nombre,usuario_2.nombre_cuenta)
    sucursal_posadas.usuarios_por_suscripcion()
    sucursal_posadas.empleados_sucursal()

    sucursal_posadas.listado_libros()

    """ sucursal_posadas.eliminar_libro(libro_1)
    sucursal_posadas.listado_libros()
    sucursal_posadas.eliminar_usuario(usuario_1)
    sucursal_posadas.usuarios_por_suscripcion()
    sucursal_posadas.eliminar_empleado(empleado_1)
    sucursal_posadas.empleados_sucursal() """
    sucursal_posadas.dinero_recaudado()

    sucursal_posadas.devolver_libro(libro_2.nombre,usuario_2.nombre_cuenta)
    sucursal_posadas.listado_libros()
    #usuario_1.listado_libros()

if __name__ == '__main__':
    main()