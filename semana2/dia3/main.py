# Jinja viene incorporado en flask
from flask import Flask, render_template
from flask.globals import request
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# para generar plantillas con bootstrap
Bootstrap(app)

lstProductos = ['laptop', 'impresora HP', 'silla gamer']

@app.route('/')
def index():
    # importar render_template para poder levantar el archivo html
    # solo carga des una carpeta llamada template (no cambiar ese nombre)
    name = request.args.get('n','invalido')
    user_ip = request.remote_addr
    
    # creamos un diccinario para pasar al index
    context = {
        'nombre': name,
        'user_ip': user_ip,
        'productos': lstProductos
    }
    # pasar la variable nombre al html: nombre=name
    # si es diccionario con doble *
    return render_template('index.html', **context)

@app.route('/productos')
def productos():
    
    context = {
        'productos': lstProductos
    }
    
    return render_template('productos.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
