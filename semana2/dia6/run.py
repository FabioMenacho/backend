# instalar: pip install flask
# instalar: pip install flask-sqlalchemy
# instalar: pip install marshmallow-sqlalchemy
# instalar: pip install flask-marshmallow
# instalar: pip install pymysql
from flask import Flask
# para devolver json y no html
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = mysql+libreria://usuario:clave@servidor/base de datos creada
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# clases para bd
# representa la tabla x eso le hacen las consultas
class Alumno(db.Model):
    # al poner primary key ya es autoincrement
    # falta ver la actualizacion de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    
    def __init__(self, nombre, email):
        self.nombre=nombre
        self.email=email

db.create_all()
        
class AlumnosSchema(ma.Schema):
    # determina que campos retornar 
    class Meta:
        fields = ('id', 'nombre', 'email')
        
#para retornar 1 alumno
alumno_schema = AlumnosSchema()
#para retornar todos los alumnos
alumnos_schema = AlumnosSchema(many=True)

@app.route('/')
def index():
    # para comprobar que es un json lo verificamos con postman
    return jsonify({'mensaje':'Bienvenido a mi API REST'})

@app.route('/setAlumno',methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    email = request.json['email']    
    
    # equivalente a insert into alumno values
    nuevoAlumno = Alumno(nombre, email)
    db.session.add(nuevoAlumno)
    db.session.commit()
    
    return alumno_schema.jsonify(nuevoAlumno)

@app.route('/alumnos',methods=['GET'])
def getAlumnos():
    # select * from alumnos
    listadoAlumno = Alumno.query.all()
    print(listadoAlumno)
    dataAlumnos = alumnos_schema.dump(listadoAlumno)
    print(dataAlumnos)
    
    return jsonify(dataAlumnos)

@app.route('/getAlumno/<id>', methods=['GET'])
def getAlumno(id):
    # select * from where id=
    alumno = Alumno.query.get(id)
    print(alumno)
    
    return alumno_schema.jsonify(alumno)

@app.route('/updateAlumno/<id>', methods=['PUT'])
def updateAlumno(id):
    # select * from where id=
    alumno = Alumno.query.get(id)
    print(alumno)
    
    nombre = request.json['nombre']
    email = request.json['email']
    
    alumno.nombre = nombre
    alumno.email = email
    
    db.session.commit()
    
    return alumno_schema.jsonify(alumno)

@app.route('/delAlumno/<id>', methods=['DELETE'])
def delAlumno(id):
    alumno = Alumno.query.get(id)
    
    # delete from alumnos where id=
    db.session.delete(alumno)
    db.session.commit()

    return alumno_schema.jsonify(alumno)

if __name__ == "__main__":
    app.run(debug=True)