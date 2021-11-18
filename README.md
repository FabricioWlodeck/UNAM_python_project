# PUBLIC LIBRARY OF MISIONES
## Descripcion
Se busca un programa para llevar un control sobre las sucursales, stock y prestamos de libros, empleados y usuarios con sus respectivas suscripciones  por parte de un sistema de bibliotecas públicas para cada localidad. 
## Requerimientos
- [X] Registro, eliminacion y control de sucursales.
- [X] Lista de Sucursales, mostrando ubicacion y cantidad usuario.
- [X] Registro, eliminacion y control de Empleados.
- [X] Registro, eliminacion y control de Usuarios.
	- [X] Clasificandolo como suscripcion de estudiante o estandar dependiendo si posee o no certicado de alumno regular (se le pregunta si posee).
	- [X] Abono por atraso de devolucion en caso que se de. 
- [X] Mostrar lista de Usuarios y Empleados por sucursal.
- [X] Alta y elimacion de libros, por sucursal o en todas las sucursales.
	- En este momento solo comparamos los nombre de los libros para el proceso de ReStock.
	- El ingreso de nuevos libros se puede hacer mediante administracion , y poder hacerlo en todas o solo una sucursal, o mediante una sucursal individual directamente.
- [X] Mostrar lista de Libros por sucursal y cantidad existente por cada unidad.
	- [X] Mostrar Libros disponibles para retirar y si el libro no cuenta con stock para ser retirado mostrar quien/es lo hicieron y sus plazos de devolucion.
- [X] Mostrar lista de Libros retirados por Usuario y su plazo de devolucion

- [ ] USAR LIBRERIA TIME PARA TODO LAS FECHAS
- AL DEVOLVER Libros SE LE PASA UN ARRAY DE LOS LIBROS A DEVOLVER
- [X] USAR ARRAY PARA SELECCIONAR LIBROS A RETIRAR
- [~] MANEJAR MULTIPLES SUCURSALES

## CORRECCION DOCENTE
- [X] Contabilizar cantidad de Usuarios por tipo de Suscripcion  
- [X] Contabilizar cantidad de Usuarios por Sucursales
- [ ] Contabilizar Libros mas Retiro por Sucursal y General\
- [ ] Contabilizar retiros por Usuarios y rankearlos
- [ ] Contabilizar cantidad de retiros por Sucursal