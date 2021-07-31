# de la libreria flask importar la clase Flask
from flask import Flask
# aplicación q recibe un nombre
app = Flask(__name__)
# hasta aca levanta un servidor de desarrollo (pruebas)
# debug mode off (inactivo) los cambios no son automaticos, debo deterne con ctrl+c y ejecutar de nuevo 
# running on http es la direccion, ruta por defecto, aparece error porque necesitas colocarles rutas /

# @ me permite entrar con los permisos, creo la raiz /
@app.route('/')
# index es la ruta por defecto, pude ser cualquier nombre
def index():
    # retorna un html
    return '<h1>HOLA MUNDO FLASK</h1>'

# flask tiene metodo main y lo corre es sobre todo para producción, sin eso igual corre pero en produccion se tendrá que hacer igual
if __name__ == '__main__':
# run levanta un servidor web
# debug=true para actualizarlo sin parar el sistema y cambiamos de puerto con port si queremos
    app.run(debug = True, port = 5000)
