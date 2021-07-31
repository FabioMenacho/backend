# Jinja viene incorporado en flask
from flask import Flask, render_template
from flask.globals import request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

app = Flask(__name__)

# configuracion de mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_sistemapos'

mysql = MySQL(app)

app.secret_key = "mysecretkey"

# para generar plantillas con bootstrap
Bootstrap(app)

lstProductos = ['laptop', 'impresora HP', 'silla gamer']

@app.route('/')
def index():
    # importar render_template para poder levantar el archivo html
    # solo carga des una carpeta llamada template (no cambiar ese nombre)
    # name = request.args.get('n','invalido')
    # user_ip = request.remote_addr
    
    # creamos un cursor
    cur = mysql.connection.cursor()
    # ejecuto la consulta
    cur.execute('SELECT c.id,t.nombre AS tipo,c.nro_doc AS nro,c.nombre AS cliente, c.telefono,c.email FROM clientes c JOIN tipo_doc t ON c.tipo_doc_id = t.id')
    # retorna el ejecute en la variable data
    data = cur.fetchall()
    # cerramos el pedido a la bae de datos
    cur.close()
    
    print(data)
    context = {
        'data': data
    }
    
    # creamos un diccinario para pasar al index
    # context = {
    #     'nombre': name,
    #     'user_ip': user_ip,
    #     'productos': lstProductos
    # }
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
    
