
alumnos = []
alumno = {}
salir = 'no'

def createAlumno(nombre, email, celular):
    nuevoAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
    alumnos.append(nuevoAlumno)

def readAlumno():
    print("LISTADO DE ALUMNOS")
    for a in alumnos:
        print("===========")
        for clave,valor in a.items():
            print(clave + " : " + valor)

def updateAlumno():
    print("ACTUALIZAR ALUMNO")
    posAlumno= -1
    alumnoBusqueda = input("INGRESE EL NOMBRE DEL ALUMNO: ")
    for i in range(len(alumnos)):
        a = alumnos[i]
        print("===========")
        for clave,valor in a.items():
            if valor == alumnoBusqueda:
                print(a)
                posAlumno = i
                print("Posición del alumno: " + str(posAlumno))
                break
            
    print("REGISTRO DE ALUMNOS:")
    nombre = input("Nombre:")
    email = input("Email:")
    celular = input("Celular:")
    actAlumno = {
        'nombre': nombre,
        'email': email,
        'celular': celular
    }
    del alumnos[posAlumno]
    alumnos.insert(posAlumno,actAlumno)

def menuopciones():
    print("*" * 20)
    print("[1] REGISTRAR ALUMNO")
    print("[2] MOSTRAR ALUMNO")
    print("[3] ACTUALIZAR ALUMNO")
    print("[4] ELIMINAR ALUMNO")
    print("*" * 20)
    
while(salir == 'no'):
    menuopciones()
    opcion = input("INGRESE OPCIÓN: ")
    if(opcion == "1"):
        # print("Registrar alumnos")
        print("REGISTRO DE ALUMNOS:")
        nombre = input("Nombre:")
        email = input("Email:")
        celular = input("Celular:")
        createAlumno(nombre,email,celular)
        
    elif(opcion =="2"):
        # print("Mostrar alumnos")
        readAlumno()
        
    elif(opcion =="3"):
        # print("Actualizar alumnos")
        updateAlumno()
                
    elif(opcion =="4"):
        print("Eliminar alumnos")
    
    else:
        print("MARCÓ UNA OPCION INCORRECTA")
        continue
    
    print("¿Desea salir del programa?")  
    salir = input()  