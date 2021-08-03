# Jinja viene incorporado en flask
# instalar: pip install flask-mysqldb
# instalar: pip install flask-bootstrap4
# instalar: pip install flask-wtf
from flask import Flask, render_template, redirect, url_for
from flask.globals import request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
# campos de texto y botones de envio
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

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

# formularios
class frmProducto(FlaskForm):
    categoria = StringField('Categoria: ',validators=[DataRequired()])
    nombre = StringField('Nombre: ',validators=[DataRequired()])
    marca = StringField('Marca: ',validators=[DataRequired()])
    modelo = StringField('Modelo: ',validators=[DataRequired()])
    serie = StringField('Nro Serie: ',validators=[DataRequired()])
    ram = StringField('Memoria RAM: ',validators=[DataRequired()])
    procesador = StringField('Procesador: ',validators=[DataRequired()])
    discoduro = StringField('Discoduro: ',validators=[DataRequired()])
    precio = StringField('Precio: ',validators=[DataRequired()])
    stock = StringField('Stock: ',validators=[DataRequired()])
    submit = SubmitField('Registrar nuevo producto')
    

@app.route('/')
def index():    
    # solo carga des una carpeta llamada template (no cambiar ese nombre)
    # name = request.args.get('n','invalido')
    # user_ip = request.remote_addr
    # return render_template('index.html', nombre=name, user_ip=user_ip)
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
    # si es diccionario con doble *
    # importar render_template para poder levantar el archivo html
    return render_template('index.html', **context)

@app.route('/productos', methods=['GET','POST'])
def productos():
    
    # cursor categorias
    curCategoria = mysql.connection.cursor()
    curCategoria.execute('SELECT * FROM cat_producto')
    dataCategoria = curCategoria.fetchall()
    curCategoria.close()
    
    catId = 0
    
    if request.method == 'POST' and int(request.form['categoria']) > 0:
        catId = request.form['categoria']
        sqlProducto = "select * from producto where cat_producto_id=" + catId
    else:
        sqlProducto = "select * from producto"
    # cursor productos
    curProducto = mysql.connection.cursor()
    curProducto.execute(sqlProducto)
    dataProducto = curProducto.fetchall()
    curProducto.close()
    
    frmNuevoProducto = frmProducto()
    
    context = {
        'dataCategoria': dataCategoria,
        'dataProducto': dataProducto,
        'catId':catId,
        'frmProducto': frmNuevoProducto
    }
    
    if frmNuevoProducto.validate_on_submit():
        # data trae la información, el valor
        categoriaId = frmNuevoProducto.categoria.data
        nombre = frmNuevoProducto.nombre.data
        marca = frmNuevoProducto.marca.data
        modelo = frmNuevoProducto.modelo.data
        serie = frmNuevoProducto.serie.data
        ram = frmNuevoProducto.ram.data
        procesador = frmNuevoProducto.procesador.data
        discoduro = frmNuevoProducto.discoduro.data
        precio = frmNuevoProducto.precio.data
        stock = frmNuevoProducto.stock.data
        
        curNuevoProducto = mysql.connection.cursor()
        curNuevoProducto.execute("INSERT INTO producto(cat_producto_id, nombre, marca, modelo, nro_serie, mem_ram, procesador, disco_duro, precio, stock) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(categoriaId, nombre, marca, modelo, serie, ram, procesador, discoduro, precio, stock))
        mysql.connection.commit()
        
        return redirect(url_for('productos'))
        
    return render_template('productos.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
