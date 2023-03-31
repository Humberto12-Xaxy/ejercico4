class Persona:

    def __init__(self, nombre, edad, telefono) -> None:
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} Edad: {self.edad} Telefono: {self.telefono}'
        