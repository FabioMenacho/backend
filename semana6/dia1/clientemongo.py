from pymongo import MongoClient

# creo una conexion de cliente a mongoDB
cliente = MongoClient('mongodb://127.0.0.1:27017')
# accediendo a la bd
db = cliente['bootcamp']
# accediendo a la colección alumno
colAlumnos = db["alumno"]

# print(colAlumnos.find())

# para imprimir un diccionario
# for a in colAlumnos.find():
#     print(a)
    
aluId = colAlumnos.insert_one({"nombre":"Hilda","email":"hilda@gmail.com","nota":0})

# para imprimir algunos elementos del diccionario
for a in colAlumnos.find():
    print(a["nombre"] + " - " + a["email"])

