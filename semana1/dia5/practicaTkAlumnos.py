from tkinter import *
from tkinter.ttk import Treeview
import sqlite3


class Alumno:
    
    db_name = 'pdatabase.s3db'
    
    def ejecutarSql(self, sql, parametros = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(sql, parametros)
            conn.commit()
        return resultado
    
    def readAlumnos(self):
        rsAlumnos = self.trvAlumnos.get_children()
        for a in rsAlumnos:
            self.trvAlumnos.delete(a)
        
        sqlAlumnos = 'select * from alumnos'
        resultado = self.ejecutarSql(sqlAlumnos)
        for fila in resultado:
            self.trvAlumnos.insert('',0,text=fila[0], values=(fila[1],fila[2]))
    
    def createAlumno(self):
        
        sqlInsertAlumno = "insert into alumnos values(?,?,?)"
        parametros = (self.nombre.get(), self.email.get(), self.celular.get())
        self.ejecutarSql(sqlInsertAlumno, parametros)
        self.readAlumnos()
    
    def __init__(self, window):
        self.wind = window
        self.wind.title('Alumnos')
    
        frame = LabelFrame(self.wind, text="Registro de nuevo alumno")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        lbNombre = Label(frame, text='Nombre: ')
        lbNombre.grid(row=1, column=0)
        self.nombre = Entry(frame)
        self.nombre.grid(row=1, column=1)
        
        lbEmail = Label(frame, text = 'Email: ')
        lbEmail.grid(row=2,column=0)
        self.email = Entry(frame)
        self.email.grid(row=2,column=1)
        
        lbCelular = Label(frame, text = 'Celular: ')
        lbCelular.grid(row=3,column=0)
        self.celular = Entry(frame)
        self.celular.grid(row=3,column=1)
        
        btnNuevoAlumno = Button(frame, text='Registrar alumno', command = self.createAlumno)
        btnNuevoAlumno.grid(row=4, columnspan = 2, sticky=W + E)
     
        self.trvAlumnos = Treeview(height=10, columns=('#1','#2'))
        self.trvAlumnos.grid(row=5, column=0, columnspan=2)
        self.trvAlumnos.heading('#0',text='Nombre', anchor=CENTER)
        self.trvAlumnos.heading('#1',text='Email', anchor=CENTER)
        self.trvAlumnos.heading('#2',text='Celular', anchor=CENTER)
        
        self.readAlumnos()
        
window = Tk()
app = Alumno(window) 
window.mainloop()