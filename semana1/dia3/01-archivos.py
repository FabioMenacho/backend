# a=adicionar
# w=escribir
# r=leer
# f y fr son variables, se puede colocar cualquier letra o nombre

# crear un archivo y escribir en él
# f = open('alumnos.txt','a')
# print("REGISTRO ALUMNO: ")
# nombre = input("NOMBRE: ")
# email = input("EMAIL: ")
# celular = input("CELULAR: ")
# # \n para salto de linea
# f.write('\n' + nombre + "," + email + "," + celular)
# f.close()

# leer un archivo ya creado
# fr = open('alumnos.txt','r')
# alumno = fr.read()
# print(alumno)
# fr.close()

# #recorre cada letra 
# for a in alumnos:
#     print(a)
#     print("=" *10)

fr = open('alumnos.txt','r')
alumnos = fr.read()
print(alumnos)

lstAlumnosData = []

# crea una lista con los datos de cada salto de linea
lstAlumnos = alumnos.splitlines()
print(lstAlumnos)

for objAlumno in lstAlumnos:
        # crea una lista con los datos separados por comas
        lstObjAlumno = objAlumno.split(',')
        # crea un diccionario con los elementos de la lista lstObjAlumno
        nombre = lstObjAlumno[0]
        email = lstObjAlumno[1]
        celular = lstObjAlumno[2]
        dictAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
        # Agrega cada diccionario a la lista lstAlumnosdata
        lstAlumnosData.append(dictAlumno)
print(lstAlumnosData)
    
fr.close()