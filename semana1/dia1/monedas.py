# formato para convertir monedas

print ("==================")
print ("   CAMBISTA 1.0   ")
print ("==================")

tc=0
while (tc != 1): 
    print ("Ingresa el valor en dólares:")
    moneda = float(input())
    print ("ingrese la moneda a convertir")
    monedaConvertir = input()
    if monedaConvertir == "soles":
        tc = 3.98
    elif monedaConvertir == "euros":
        tc = 0.85
    else:
        tc = 1
            
    soles = moneda*tc
    if(soles == moneda):
        print ("No indicó una moneda válida ADIOS!!!")
    else:
        print ("El valor en "+ monedaConvertir +" es de " + str(soles))