class Sucursal():
    def __init__(self, direccion, personal, lista_libros, usuarios, horarios_atencion, dinero_recaudado):
        self.__direccion = direccion
        self.__personal = personal
        self.__lista_libros = [] #lista de objetos Libro
        self.__usuarios = [] #lista de objetos Usuario
        self.__horarios_atencion = horarios_atencion
        self.__dinero_recaudado = dinero_recaudado
