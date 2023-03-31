from Persona import Persona
from Cliente import Cliente
from Trabajador import Trabajador

if __name__ == '__main__':

    persona = Persona('Humberto', 21, '9661183289')
    
    print(persona)

    cliente = Cliente('Salvador', 63, '0123456789', 4500)
    print(cliente)

    trabajador = Trabajador('Ingrid', 19, '9667894561', 10000)
    print(trabajador) 