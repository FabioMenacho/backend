# Variables en python

# name = "Fabio"
# print ("Hola " + name)
# print ("Hola mi nombre es Fabio, cuál es tu nombre")
# name = input()
# print ("mucho gusto en conocerte " + name)
# print ("Vamos a sumar 2 numeros")

# si no coloco el tipo de dato lo considera string por eso no suma
n1 = input ("ingresa el valor de n1:")
n2 = input ("ingresa el valor de n2:")
# suma = n1 + n2
# print ("La suma de " + n1 + " + " + n2 + " es " + suma)

n1 = int(n1)
n2 = int(n2)
suma = n1 +n2
print ("La suma de " + str(n1) + " + " + str(n2) + " es " + str(suma))

resta = n1 - n2
print ("la resta de ",n1," - ",n2," es ", resta)

