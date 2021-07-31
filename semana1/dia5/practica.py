class vehiculo:
    def __init__(self, mar, km, col):
        self.marca = mar
        self.km = km
        self.color = col  
              
    def encender(self):
        print("Encendiendo vehículo...")
    

class camion(vehiculo):
    def __init__(self, mar, km, col, ej):
        super().__init__(mar, km, col)
        self.ejes = ej
        
    def arrancar(self):
        print("Arrancando el camión...")
    

carro = vehiculo('suzuki', 160000, 'rojo')
# carro.encender()

hino = camion('hino', 0, 'azul', 8)
hino.encender()
hino.arrancar()


class rectangulo():
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def areaR(self):
        return self.ancho * self.alto
            

class cuadrado():
    def __init__(self, lado):
        self.lado = lado
        
    def areaC(self):
        return self.lado * self.lado
    

class figura(rectangulo, cuadrado):
    def __init__(self, tipo, v1, v2=0):
        rectangulo.__init__(self, v1, v2)
        cuadrado.__init__(self, v1)
        self.tipo = tipo
    
    def area(self):
        if self.tipo == rectangulo:
            return rectangulo.areaR(self)
        elif self.tipo == "cuadrado":
            return cuadrado.areaC(self)
        
        

r = rectangulo(20,30)
arear = r.areaR()
print("Area del rectangulo: " + str(arear))

c = cuadrado(20)
areac = c.areaC()
print("Area del cuadrado: " + str(areac))

f = figura(rectangulo, 20, 30)
areaf = f.areaR()
print("Area de la figura: " + str(areaf))

g = figura(cuadrado, 20)
areag = g.areaC()
print("Area de la figura: " + str(areag))

h = figura(rectangulo, 20, 30)
areah = h.area()
print("Area de la figura: " + str(areah))