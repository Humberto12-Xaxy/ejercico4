from Persona import Persona

class Cliente(Persona):

    def __init__(self, nombre, edad, telefono, credito) -> None:
        super().__init__(nombre, edad, telefono)
        self.credito = credito

    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} Edad: {self.edad} Telefono: {self.telefono} Credito: {self.credito}'