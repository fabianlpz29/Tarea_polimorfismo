class Vidri:
    pass

    def __init__(self, producto):
        self.producto =  producto

objeto1 =  Vidri("Letrero")
objeto2 = Vidri("martillo")

class cliente1(Vidri):
    pass

    def Comprar():
        return 'Compre un {}'.format(objeto1.producto)
    
class cliente2(Vidri):
    pass

    def Comprar():
        return 'Compre un {}'.format(objeto2.producto)
    
user1 = cliente1
user2 = cliente2

print(user1.Comprar())
print(user2.Comprar())
    