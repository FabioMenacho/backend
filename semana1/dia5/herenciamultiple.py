class Rectangulo:
    
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def area(self):
        return self.ancho * self.alto
    
r = Rectangulo(20,30)
areaR = r.area()
# print("Area del rectangulo: " + str(areaR))


class Cuadrado:
    
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado * self.lado
    
c = Cuadrado(20)
areaC = c.area()
# print("Area del cuadrado: " + str(areaC))

class FiguraGeometrica(Rectangulo, Cuadrado):
    
    def __init__(self, tipo, v1, v2=0):
        self.tipo = tipo
        Rectangulo.__init__(self, v1, v2)
        Cuadrado.__init__(self, v1)
        
        def area(self):
            if self.tipo == "Rectangulo":
                return Rectangulo.area(self)
            else:
                return Cuadrado.area(self)
        
        # Rectangulo.alto = alto
        # Rectangulo.ancho = ancho
        
f = FiguraGeometrica("Rectangulo",20,10)
area = f.area()
print("Area del rectangulo: " + str(area))

f = FiguraGeometrica("Cuadrado",20,10)
area = f.area()
print("Area del cuadrado: " + str(area))
        