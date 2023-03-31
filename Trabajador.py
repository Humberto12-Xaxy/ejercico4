from Persona import Persona

class Trabajador(Persona):

    def __init__(self, nombre, edad, telefono, salario) -> None:
        super().__init__(nombre, edad, telefono)
        self.salario = salario

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} Edad: {self.edad} Telefono: {self.telefono} Salario: {self.salario}'