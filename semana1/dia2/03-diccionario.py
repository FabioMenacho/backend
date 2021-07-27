#  manejo de diccionarios

capitales = {'Perú':'Lima', 'Ecuador':'Quito', 'Chile':'Santiago','Uruguay':'Montevideo','Brasil':'Brasilia'}
print (capitales)

capital = {'USA':'Washington DC'}
capitales.update(capital)
print (capitales)

alumnos = {
    'nombre':'Fabio Menacho',
    'email':'fmenacho@uni.pe',
    'celular':'997064940'
}
print(alumnos['email'])

alumnoModelo = alumnos.copy()

alumnos['email'] = 'fabio_m_82@yahoo.es'
print(alumnos['email'])

print(alumnoModelo['email'])

alumnos.pop('celular')
print(alumnos)

a = alumnos.pop('dni','No existe DNI')
print(a)

# eliminar un diccionario
# alumnos = {}
# alumnoModelo.clear()
# print(alumnos)
# print(alumnoModelo)

print(alumnos.keys())
print(alumnos.values())

for clave in alumnos.items():
    print(clave,alumnos[clave])
    
for clave in alumnos.keys():
    print(clave,alumnos[clave])
    
for clave,valor in alumnos.items():
    print(clave,valor)