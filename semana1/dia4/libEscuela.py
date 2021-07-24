class clsPersona:    
    def __init__(self, nom, ema, cel):
        self.nombre = nom
        self.email = ema
        self.celular = cel
    
    def registrarse(self):
        pass


class clsUsuario:    
    def __init__(self, user, password):
        self.nombreUsuario = user
        self.password = password
        
    def login(self):
        pass
        

# herencia multiple
class clsProfesor(clsPersona, clsUsuario):    
    def __init__(self, nom, ema, cel, esp, u, p):
        clsPersona.__init__(self, nom, ema, cel)
        clsUsuario.__init__(self,u ,p)
        self.especialidad = esp

    def calificar(self):
        pass


class clsAlumno:
    # atributos
    def __init__(self, nom, ema, cel ):
        self.nombre = nom
        self.email = ema
        self.celular = cel
        
    def enviarEjercicio(self):
        pass
    
    
class clsCurso:
    def __init__(self, cod, nom, nota):
        self.codigo = cod
        self.nombre = nom
        self.nota = nota
        
    
    # funciones normalmente se usan en SQL
    def create(self):
        pass
    
    def read(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
    