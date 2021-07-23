from libAlumno import *

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
        alumnos = createAlumno(nombre,email,celular,alumnos)
        
    elif(opcion =="2"):
        readAlumno(alumnos)
        
    elif(opcion =="3"):
        updateAlumno(alumnos)
                
    else:
        print("MARCÓ UNA OPCION INCORRECTA")
        continue
    
    print("¿Desea salir del programa?")  
    salir = input()  
    if(salir == "si"):
        strAlumnosGrabar = grabarAlumnos(alumnos)
        fw =open('alumnos.txt', 'w')
        fw.write(strAlumnosGrabar)
        fw.close()
        