from persona import Persona


class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, horario, cargo, sueldo):
        super().__init__(nombre, apellido, edad)
        self.__horario = horario  # diccionario de 5 dias de la semana 8 horas diarias
        self.__cargo = cargo
        self.__sueldo = sueldo

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, value):
        self.__horario = value

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, value):
        self.__cargo = value

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, value):
        self.__sueldo = value

    def __str__(self):
        texto = (f'Empleado: {self.nombre}, {self.apellido} \nCargo: {self.cargo} \nSueldo: ${self.sueldo} ')
        return texto

""" horarios = {'Lunes':8 , 'Martes':8, 'Miercoles':8, 'Jueves':8, 'Viernes':8}
cargo = 'repositor'
sueldo = 55000 """
