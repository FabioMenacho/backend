# Programa para bucles

n = int(input("ingrese tabla de multiplicar:"))
# el último valor es para indicarle el aumento
for x in range(1,13,2):
    tabla = n * x
    print(str(n) + " x " + str(x) + " = " + str(tabla))


# nombre = input("ingresa tu nombre: ")
# for n in nombre:
#     print(n)

i=1
while i<12:
    tabla = n * i
    print(str(n) + " x " + str(i) + " = " + str(tabla))
    i+=1