from practicaLibAlumno import *

# definir variables de entrada y salida

alumnos = []
alumno = {}
salir = 'no'

fr = open('alumnos.csv','r')
fAlumnos = fr.read()
alumnos = cargarAlumnos(fAlumnos)
# print(alumnos)
fr.close

while(salir == 'no'):
    menuopciones()
    opcion = input("INGRESE OPCIÓN: ")
    if(opcion == "1"):
        print("REGISTRO DE NUEVO ALUMNO:")
        nombre = input("NOMBRE:")
        email = input("EMAIL:")
        celular = input("CELULAR:")
        alumnos = createAlumno(nombre,email,celular,alumnos)
        # print(alumnos)
        
    elif(opcion =="2"):
        print("Mostrar alumnos")
        readAlumno(alumnos)
        
    elif(opcion =="3"):
        print("Actualizar alumnos")
        updateAlumno(alumnos)
        
    elif(opcion =="4"):
        print("Eliminar alumnos")
                
    else:
        print("MARCÓ UNA OPCION INCORRECTA")
        continue
    
    print("¿Desea salir del programa?")  
    salir = input()  
    if(salir == "si"):
        strAlumnosGrabar = grabarAlumnos(alumnos)
        fw =open('alumnos.csv', 'w')
        fw.write(strAlumnosGrabar)
        fw.close()