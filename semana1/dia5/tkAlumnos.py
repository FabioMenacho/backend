from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

class Alumno:
    
    db_name = 'database.s3db'
    
    # funcion para relacionar con la base de dato
    def ejecutarSql(self, sql, parametros = ()):
        with sqlite3.connect(self.db_name) as conn:
            # posicionar en la base de datos: click derecho agregar consulta
            cursor = conn.cursor()
            resultado = cursor.execute(sql, parametros)
            conn.commit()
        return resultado
    
    def readAlumnos(self):
        rsAlumnos = self.trvAlumnos.get_children()
        #limpiando la tabla
        for a in rsAlumnos:
            self.trvAlumnos.delete(a)
            
        sqlAlumnos = 'select * from alumnos'
        resultado = self.ejecutarSql(sqlAlumnos)
        # print(resultado)
        for fila in resultado:
            self.trvAlumnos.insert('', 0, text=fila[0], values=fila[1])
        
    def createAlumno(self):
        sqlInsertAlumno = "insert into alumnos values(?,?)"
        # coger los valores ingresados
        parametros = (self.nombre.get(),self.email.get())
        # guardar el alumno nuevo
        self.ejecutarSql(sqlInsertAlumno,parametros)
        # mostrar los valores
        self.readAlumnos()
    
    # window es una clase que hace la interfaa q pertenece a la libreria tkinter
    def __init__(self, window):
        self.wind = window
        self.wind.title('Alumnos')
        
        # Creamos un frame (marco)
        frame = LabelFrame(window,text = "Registro de nuevo alumno")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Campos del formulario
        # Campo nombre
        lbNombre = Label(frame, text = 'Nombre: ')
        lbNombre.grid(row=1,column=0)
        # otra forma es:
        # Label(frame, text = 'Nombre: ').grid(row=1,column=0)
        # capturo la caja con self.nombre, la variable seria nombre dentro del frame window
        self.nombre = Entry(frame)
        self.nombre.grid(row=1,column=1)
        
        # Campo email
        lbEmail = Label(frame, text = 'Email: ')
        lbEmail.grid(row=2,column=0)
        self.email = Entry(frame)
        self.email.grid(row=2,column=1)
        
        # Campo celular
        lbCelular = Label(frame, text = 'Celular: ')
        lbCelular.grid(row=3,column=0)
        self.celular = Entry(frame)
        self.celular.grid(row=3,column=1)
        
        # Boton para crear nuevo alumno
        btnNuevoAlumno = Button(frame, text = "Registrar alumno", command=self.createAlumno)
        # sticky para alargar el boton en todo el ancho
        btnNuevoAlumno.grid(row=4, columnspan = 2, sticky=W + E)
        
        self.trvAlumnos = Treeview(height=10,columns=2)
        self.trvAlumnos.grid(row=5,column=0,columnspan=2)
        self.trvAlumnos.heading('#0',text='Nombre',anchor=CENTER)
        self.trvAlumnos.heading('#1',text='Email',anchor=CENTER)
        # trvAlumnos.heading('#2',text='Celular',anchor=CENTER)
        
        self.readAlumnos()
        

window = Tk()
app = Alumno(window)
window.mainloop() 
