class Salida:
    pass

    def __init__(self,destino):
        self.destino = destino

salida1 = Salida("San miguel")
salida2 = Salida("Berlin") 

class Juan(Salida):
    pass

    def SalirPaseo():
        return 'Juan saldra a pasear a {}'.format(salida1.destino)
    
class Daniela(Salida):
    pass

    def SalirPaseo():
        return 'Daniela saldra a pasear a {}'.format(salida2.destino)
    
juan = Juan
daniela = Daniela

print(juan.SalirPaseo())
print(daniela.SalirPaseo())