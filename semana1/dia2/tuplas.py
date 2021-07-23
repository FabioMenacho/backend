#  Manejo de tuplas
#  a las tuplas no se le pueden agregar ni quitar valores
#  ocupa menos memoria
#  para valores que no van a cambiar en el tiempo
primos = (2,3,5,7,11,13)
pares = [2,4,6,8,10]
dias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")

# no se puede
# primos.pop()

print(primos)
primos2 = list(primos)
primos2.pop()
primos = tuple(primos2)
print(primos)
primosordenados=sorted(primos)
print(primosordenados)
primosordenados=sorted(primos,reverse=True)
print(primosordenados)

# print (dias[2])
# print (max(primos))
# print (max(pares))