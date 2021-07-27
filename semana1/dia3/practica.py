# f = open('alumnos.csv','a')
# print("REGISTRO ALUMNO: ")
# nombre = input("NOMBRE: ")
# email = input("EMAIL: ")
# celular = input("CELULAR: ")

# f.write(nombre + "," + email + "," + celular + '\n')
# f.close()

# fr = open('alumnos.csv','r')
# alumno = fr.read()
# print(alumno)
# fr.close()

fr = open('alumnos.csv','r')
alumnos = fr.read()
print(alumnos)

lstAlumnosData = []

lstAlumnos = alumnos.splitlines()
print(lstAlumnos)

for objAlumno in lstAlumnos:
        lstObjAlumno = objAlumno.split(',')
        print(lstObjAlumno)
        nombre = lstObjAlumno[0]
        email = lstObjAlumno[1]
        celular = lstObjAlumno[2]
        dictAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }        
        print(dictAlumno)
        lstAlumnosData.append(dictAlumno)
print(lstAlumnosData)

fr.close()