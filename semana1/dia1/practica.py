# a = int(input("Ingresa el primer valor: "))
# b = int(input("Ingresa el segundo valor: "))
# # suma = a+b
# print ("La suma es: " + str(a+b))


# tc=0
# while tc!=1:
#     print("Ingresa el valor en dolares: ")
#     moneda = float(input())
#     print("Ingrese la moneda a convertir: ") 
#     monedaConvertir = input()
#     if monedaConvertir == "soles":
#         tc = 3.98
#     elif monedaConvertir == "euros":
#         tc = 0.85
#     else:
#         tc = 1
        
#     cambio = moneda * tc
#     if cambio == moneda:
#         print("No ingresó un tc válido...adios!!!")
#     else:
#         print("El tipo de cambio por " + str(moneda) + " dólares es: " + str(cambio) + " soles")
    

n = int(input("Ingrese número para multiplicar: "))
# print(n)
for x in range(n):
    print(str(n) + " x " + str(x) + " = " + str(x*n))