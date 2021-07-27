
def menuopciones():
    print("*" * 20)
    print("[1] REGISTRAR ALUMNO")
    print("[2] MOSTRAR ALUMNO")
    print("[3] ACTUALIZARAR ALUMNO")
    print("[4] ELIMINAR ALUMNO")
    print("*" * 20)
    
def grabarAlumnos(lstAlumnos):
    strAlumnos = ""
    for a in lstAlumnos:
        for clave,valor in a.items():
            strAlumnos += valor
            if clave != 'celular':
                strAlumnos += ','
            else:
                strAlumnos += "\n"
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
        dictAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
        lstAlumnosData.append(dictAlumno)
    return lstAlumnosData

def createAlumno(nombre, email, celular,alumnos):
    nuevoAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
    alumnos.append(nuevoAlumno)
    return alumnos

def readAlumno(alumnos):
    print("LISTADO DE ALUMNOS")
    for a in alumnos:
        print("===========")
        for clave,valor in a.items():
            print(clave + " : " + valor)
            
def updateAlumno(alumnos):
    print("ACTUALIZAR ALUMNO")
    posAlumno= -1
    alumnoBusqueda = input("INGRESE EL NOMBRE DEL ALUMNO: ")
    for i in range(len(alumnos)):
        a = alumnos[i]
        # print("===========")
        for clave,valor in a.items():
            if valor == alumnoBusqueda:
                print(a)
                posAlumno = i
                print("Posición del alumno: " + str(posAlumno))
                break
            
    print("ACTUALIZANDO DATOS DEL ALUMNO:")
    nombre = input("NOMBRE:")
    email = input("EMAIL:")
    celular = input("CELULAR:")
    actAlumno = {
        'nombre': nombre,
        'email': email,
        'celular': celular
    }
    del alumnos[posAlumno]
    alumnos.insert(posAlumno,actAlumno)