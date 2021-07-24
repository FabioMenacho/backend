class vehiculo:
    def __init__(self, mar, km, col):
        self.marca = mar
        self.km = km
        self.color = col
        
    def encender(self):
        print("Encendiendo...")


class auto(vehiculo):    
    def __init__(self, mar,km,col, cap):
        super().__init__(mar, km, col)
        self.capacidad = cap
        
    def prender(self):
        super().encender()
        print("Auto...")
        

class camion(vehiculo):
    def __init__(self, mar, km, col, ej):
        super().__init__(mar, km, col)
        self.ejes = ej
        
    def prender(self):
        print("Arrancando camión")


ferrari = auto('ferrari', 0, 'amarillo', 2)
ferrari.prender()

hino = camion('vw', 100000, 'verde', 8)
hino.prender()

vw = vehiculo('vw', 100, 'rojo')


