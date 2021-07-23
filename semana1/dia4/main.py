from libEscuela import clsAlumno
import os
# definir variables de entrada y salida

alumnos = []
alumno = {}
salir = 'no'

def menuopciones():
    print("*" * 20)
    print("[1] REGISTRAR ALUMNO")
    print("[2] MOSTRAR ALUMNO")
    print("[3] ACTUALIZARAR ALUMNO")
    print("[4] ELIMINAR ALUMNO")
    print("*" * 20)

def cargarAlumnos(strAlumnos):
    # lista de objetos
    lstAlumnosData = []

    lstAlumnos = strAlumnos.splitlines()
    # print(lstAlumnos)

    for objAlumno in lstAlumnos:
        # creo una lista con la separación de comas
        lstObjAlumno = objAlumno.split(',')
        nombre = lstObjAlumno[0]
        email = lstObjAlumno[1]
        celular = lstObjAlumno[2]
        nuevoAlumno = clsAlumno(nombre, email, celular)
        lstAlumnosData.append(nuevoAlumno)
    return lstAlumnosData

def mostrarAlumnos():
    print("==================")
    print("LISTADO DE ALUMNOS")
    print("==================")
    for a in alumnos:
        print(a.nombre + " | " + a.email + " | " + a.celular)
        print("==================")

def grabarAlumnos():
    strAlumnos = ""
    for a in alumnos:
        strAlumnos += "\n" + a.nombre + "," + a.email + "," + a.celular
    return strAlumnos

fr = open('alumnos.txt','r')
fAlumnos = fr.read()
alumnos = cargarAlumnos(fAlumnos)
fr.close

while(salir == 'no'):
    menuopciones()
    opcion = input("INGRESE OPCIÓN: ")
    if(opcion == "1"):
        print("REGISTRO DE NUEVO ALUMNO:")
        nombre = input("NOMBRE:")
        email = input("EMAIL:")
        celular = input("CELULAR:")
        nAlumno = clsAlumno(nombre, email, celular)
        alumnos.append(nAlumno)
        
    elif(opcion =="2"):
        mostrarAlumnos()
        
    elif(opcion =="3"):
        pass
                
    else:
        print("MARCÓ UNA OPCION INCORRECTA")
        continue
    
    print("¿Desea salir del programa?")  
    salir = input()  
    if(salir == "si"):
        strAlumnosGrabar = grabarAlumnos()
        fw =open('alumnos.txt', 'w')
        fw.write(strAlumnosGrabar)
        fw.close()
        