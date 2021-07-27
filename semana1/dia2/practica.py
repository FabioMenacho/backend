from random import choice
# primos = [2,3,5,7,11,13]
# dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
# fecha = ["martes", 20, "Julio", 2021]

# primos.append(17)
# primos.insert(0,1)


# for p in primos[0:len(primos):2]:
#     print(p)
    
    
# pares = (2,4,6,8,10,12)
# print(pares)
# pares1 = list(pares)
# print(pares1)
# pares1.pop(2)
# print(pares1)
# pares = tuple(pares1)
# print(pares)
# paresordenados = sorted(pares, reverse=True)
# print(paresordenados)

alumnos = {
    'nombre':'Fabio Menacho Landa',
    'email':'fmenacho@uni.pe',
    'celular':'997064940'
}
print(alumnos)
print(alumnos['email'])
print(alumnos.keys())
print(alumnos.values())

for key in alumnos.keys():
    print(key)
print(alumnos.keys())
    
for value in alumnos.values():
    print(value)
print(alumnos.values())

for a in alumnos.items():
    print(a)
    
for key,value in alumnos.items():
    print(key,value)

print(alumnos.items())

# copiaAlumnos = alumnos.copy()
# print(copiaAlumnos)

# copiaAlumnos['email']='fabio_m_82@yahoo.es'
# print(copiaAlumnos)

# alumnos.pop('celular')
# print(alumnos)


dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
azar = choice(dias)
print(azar)