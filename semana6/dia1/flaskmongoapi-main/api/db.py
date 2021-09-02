from bson.json_util import dumps, ObjectId
from flask import current_app
from pymongo import MongoClient, DESCENDING
from werkzeug.local import LocalProxy


# Este método se encarga de configurar la conexión con la base de datos
def get_db():
    mongo_db = current_app.config['DB_URI']
    client = MongoClient(mongo__db)
    return client.plantilla


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def test_connection():
    return dumps(db.collection_names())


def collection_stats(collection_nombre):
    return dumps(db.command('collstats', collection_nombre))

# -----------------Carreras-------------------------


def crear_plantilla(json):
    return str('TODO')

def consultar_plantilla_por_id(plantilla_id):
    return str('TODO')

def actualizar_plantilla(carrera):
    return str('TODO')

def borrar_plantilla_por_id(plantilla_id):
    return str('TODO')

def consultar_plantillas(skip, limit):
    return str('TODO')
