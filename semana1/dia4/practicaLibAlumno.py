from practicaLibEscuela import clsAlumno

def menuopciones():
    print("*" * 20)
    print("[1] REGISTRAR ALUMNO")
    print("[2] MOSTRAR ALUMNO")
    print("[3] ACTUALIZARAR ALUMNO")
    print("[4] ELIMINAR ALUMNO")
    print("*" * 20)
    
def grabarAlumnos(alumnos):
    strAlumnos = ""
    for a in alumnos:
      strAlumnos += a.nombre + "," + a.email + "," + a.celular + "\n"
    return strAlumnos

def cargarAlumnos(strAlumnos):
    lstAlumnosData = []

    lstAlumnos = strAlumnos.splitlines()
    # print(lstAlumnos)

    for objAlumno in lstAlumnos:
        lstObjAlumno = objAlumno.split(',')
        nombre = lstObjAlumno[0]
        email = lstObjAlumno[1]
        celular = lstObjAlumno[2]
        dictAlumno = clsAlumno(nombre, email, celular)
        lstAlumnosData.append(dictAlumno)
    return lstAlumnosData

def createAlumno(alumnos):
    nombre = input("NOMBRE:")
    email = input("EMAIL:")
    celular = input("CELULAR:")
    alumno = clsAlumno(nombre,email,celular)
    alumnos.append(alumno)
    return alumnos

def readAlumno(alumnos):
    print("LISTADO DE ALUMNOS")
    for a in alumnos:
        print("=" * 40)
        print(a.nombre, a.email, a.celular)
    print("=" * 40)
    
def updateAlumno(alumnos):
    print("ACTUALIZAR ALUMNO")
    posAlumno= -1
    alumnoBusqueda = input("INGRESE EL NOMBRE DEL ALUMNO: ")
    for a in alumnos:
        if a.nombre == alumnoBusqueda:
            print(a)
            posAlumno = posAlumno+1
            print("Posición del alumno: " + str(posAlumno))
            break
            
    print("ACTUALIZANDO DATOS DEL ALUMNO:")
    nombre = input("NOMBRE:")
    email = input("EMAIL:")
    celular = input("CELULAR:")
    alumno = clsAlumno(nombre,email,celular)
    del alumnos[posAlumno]
    alumnos.insert(posAlumno,alumno)