from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ThanathosAR:prueba1234@ThanathosAR.mysql.pythonanywhere-services.com/ThanathosAR$proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Modelos
class Cliente(db.Model):
    clienteId = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(20))
    nombreApellido = db.Column(db.String(100))
    email = db.Column(db.String(50))
    clave = db.Column(db.String(20))
    telefonoFijo = db.Column(db.String(20))
    telefonoCelular = db.Column(db.String(20))
    miembroClub = db.Column(db.Boolean, default=False)
    direccionEnvio = db.Column(db.String(200))
    pisoDeptoEnvio = db.Column(db.String(50))
    codigoPostalEnvio = db.Column(db.String(20))
    localidadEnvio = db.Column(db.String(50))
    provinciaEnvio = db.Column(db.String(50))

    # Asignación de valores con el
    # Constructor de la clase
    def __init__(self, nombreUsuario, nombreApellido, email, clave, telefonoFijo, telefonoCelular, miembroClub,
                 direccionEnvio, pisoDeptoEnvio, codigoPostalEnvio, localidadEnvio, provinciaEnvio):
        self.nombreUsuario = nombreUsuario
        self.nombreApellido = nombreApellido
        self.email = email
        self.clave = clave
        self.telefonoFijo = telefonoFijo
        self.telefonoCelular = telefonoCelular
        self.miembroClub = miembroClub
        self.direccionEnvio = direccionEnvio
        self.pisoDeptoEnvio = pisoDeptoEnvio
        self.codigoPostalEnvio = codigoPostalEnvio
        self.localidadEnvio = localidadEnvio
        self.provinciaEnvio = provinciaEnvio

class Item(db.Model):
    itemId = db.Column(db.Integer, primary_key=True)
    nombreItem = db.Column(db.String(100), db.ForeignKey('producto.nombre'))
    descripcionItem = db.Column(db.String(300), db.ForeignKey('producto.descripcion'))
    fotoItem = db.Column(db.String(200), db.ForeignKey('producto.fotoTarjeta'))
    precioItem = db.Column(db.Float, db.ForeignKey('producto.precio'))
    stockItem = db.Column(db.Integer, db.ForeignKey('producto.stock'))
    precioClubItem = db.Column(db.Float, db.ForeignKey('producto.precioClub'))

    # Asignación de valores con el
    # Constructor de la clase Item
    def __init__(self, nombreItem, descripcionItem, fotoItem, precioItem, stockItem, precioClubItem):
        self.nombreItem = nombreItem
        self.descripcionItem = descripcionItem
        self.fotoItem = fotoItem
        self.precioItem = precioItem
        self.stockItem = stockItem
        self.precioClubItem = precioClubItem

class Pedido(db.Model):
    pedidoId = db.Column(db.Integer, primary_key=True)
    usuarioComprador = db.Column(db.String(20), db.ForeignKey('cliente.clienteId'))
    total = db.Column(db.Float)
    direccionEnvio = db.Column(db.String(200), db.ForeignKey('cliente.direccionCliente'))
    pisoDeptoEnvio = db.Column(db.String(50), db.ForeignKey('cliente.pisoDeptoCliente'))
    codigoPostalEnvio = db.Column(db.String(20), db.ForeignKey('cliente.codigoPostalCliente'))
    localidadEnvio = db.Column(db.String(50), db.ForeignKey('cliente.localidadCliente'))
    provinciaEnvio = db.Column(db.String(50), db.ForeignKey('cliente.provinciaCliente'))
    formaPago = db.Column(db.String(50))

    # Lista de ítems asociados al pedido (relación con Item)
    items = db.relationship('Item', backref='pedido', lazy=True)

    # Constructor de la clase
    def __init__(self, usuarioComprador, items, total, direccionEnvio, pisoDeptoEnvio, codigoPostalEnvio, localidadEnvio, provinciaEnvio, formaPago):
        self.usuarioComprador = usuarioComprador
        self.items = items
        self.total = total
        self.direccionEnvio = direccionEnvio
        self.pisoDeptoEnvio = pisoDeptoEnvio
        self.codigoPostalEnvio = codigoPostalEnvio
        self.localidadEnvio = localidadEnvio
        self.provinciaEnvio = provinciaEnvio
        self.formaPago = formaPago

class Producto(db.Model):
    productoId = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(300))
    fotoTarjeta = db.Column(db.String(200))
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)
    precioClub = db.Column(db.Float)
    fotoTarjetaOfertaClub = db.Column(db.String(200))
    fotoCaruselOfertaClub = db.Column(db.String(200))
    fotoDestacado = db.Column(db.String(100))

    # Constructor de la clase
    def __init__(self, nombre, descripcion, fotoTarjeta, precio, stock, precioClub, fotoTarjetaOfertaClub,
                 fotoCaruselOfertaClub, fotoDestacado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fotoTarjeta = fotoTarjeta
        self.precio = precio
        self.stock = stock
        self.precioClub = precioClub
        self.fotoTarjetaOfertaClub = fotoTarjetaOfertaClub
        self.fotoCaruselOfertaClub = fotoCaruselOfertaClub
        self.fotoDestacado = fotoDestacado

# Creación de todas las tablas

with app.app_context():
    db.create_all()

# Esquemas
class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('clienteId', 'nombreUsuario', 'nombreApellido', 'email', 'clave', 'telefonoFijo', 'telefonoCelular',
                  'miembroClub', 'direccionCliente', 'pisoDeptoCliente', 'codigoPostalCliente', 'localidadCliente', 'provinciaCliente')

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

class ItemSchema(ma.Schema):
    class Meta:
        fields = ('itemId', 'nombreItem', 'descripcionItem', 'fotoItem', 'precioItem', 'stockItem', 'precioClubItem')

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

class PedidoSchema(ma.Schema):
    class Meta:
        fields = ('pedidoId', 'usuarioComprador', 'total', 'envio', 'formaPago', 'items')

pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('productoId', 'nombre', 'descripcion', 'fotoTarjeta', 'precio', 'stock', 'precioClub',
                  'fotoTarjetaOfertaClub', 'fotoCaruselOfertaClub', 'fotoDestacado')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

# Rutas de PRODUCTO para Cliente Web

@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla


@app.route('/productos/<productoId>',methods=['GET'])
def get_producto(productoId):
    producto=Producto.query.get(productoId)
    return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro


@app.route('/productos/<productoId',methods=['DELETE'])
def delete_producto(productoId):
    producto=Producto.query.get(productoId)
    db.session.delete(producto)
    db.session.commit()                     # confirma el delete
    return producto_schema.jsonify(producto) # me devuelve un json con el registro eliminado


@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente

    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    fotoTarjeta=request.json['fotoTarjeta']
    precio=request.json['precio']
    stock=request.json['stock']
    precioClub=request.json['precioClub']
    fotoTarjetaOfertaClub=request.json['fotoTarjetaOfertaClub']
    fotoCaruselOfertaClub=request.json['fotoCaruselOfertaClub']
    fotoDestacado=request.json['fotoDestacado']

    new_producto=Producto(nombre,descripcion,fotoTarjeta,precio,stock,precioClub,fotoTarjetaOfertaClub,fotoCaruselOfertaClub,fotoDestacado)
    db.session.add(new_producto)
    db.session.commit() # confirma el alta
    return producto_schema.jsonify(new_producto)


@app.route('/productos/<productoId>' ,methods=['PUT'])
def update_producto(productoId):
    producto=Producto.query.get(productoId)

    producto.nombre=request.json['nombre']
    producto.descripcion=request.json['descripcion']
    producto.fotoTarjeta=request.json['fotoTarjeta']
    producto.precio=request.json['precio']
    producto.stock=request.json['stock']
    producto.precioClub=request.json['precioClub']
    producto.fotoTarjetaOfertaClub=request.json['fotoTarjetaOfertaClub']
    producto.fotoCaruselOfertaClub=request.json['fotoCaruselOfertaClub']
    producto.fotoDestacado=request.json['fotoDestacado']

    db.session.commit()    # confirma el cambio
    return producto_schema.jsonify(producto)    # y retorna un json con el producto


# Rutas de CLIENTES para Cliente Web

@app.route('/clientes', methods=['GET'])
def get_clientes():
    all_clientes = Cliente.query.all()
    result = clientes_schema.dump(all_clientes)
    return jsonify(result)

@app.route('/clientes/<clienteId>', methods=['GET'])
def get_cliente(clienteId):
    cliente = Cliente.query.get(clienteId)
    return cliente_schema.jsonify(cliente)


@app.route('/clientes/<clienteId>',methods=['DELETE'])
def delete_producto(clienteId):
    cliente=Cliente.query.get(clienteId)
    db.session.delete(cliente)
    db.session.commit()                     # confirma el delete
    return cliente_schema.jsonify(cliente) # me devuelve un json con el registro eliminado


@app.route('/clientes', methods=['POST'])
def create_cliente():
    # Procesar datos del cliente desde request.json

    print(request.json)

    nombreUsuario=request.json['nombreUsuario']
    nombreApellido=request.json['nombreApellido']
    email=request.json['email']
    clave=request.json['clave']
    telefonoFijo=request.json['telefonoFijo']
    telefonoCelular=request.json['telefonoCelular']
    miembroClub=request.json['miembroClub']
    direccionCliente=request.json['direccionCliente']
    pisoDeptoCliente=request.json['pisoDeptoCliente']
    codigoPostalCliente=request.json['codigoPostalCliente']
    localidadCliente=request.json['localidadCliente']
    provinciaCliente=request.json['provinciaCliente']

    new_cliente = Cliente(nombreUsuario, nombreApellido, email, clave, telefonoFijo, telefonoCelular, miembroClub,
                          direccionCliente, pisoDeptoCliente, codigoPostalCliente, localidadCliente, provinciaCliente)
    db.session.add(new_cliente)
    db.session.commit()
    return cliente_schema.jsonify(new_cliente)


@app.route('/clientes/<clienteId>' ,methods=['PUT'])
def update_cliente(clienteId):
    cliente=Cliente.query.get(clienteId)

    cliente.nombreUsuario=request.json['nombreUsuario']
    cliente.nombreApellido=request.json['nombreApellido']
    cliente.email=request.json['email']
    cliente.clave=request.json['clave']
    cliente.telefonoFijo=request.json['telefonoFijo']
    cliente.telefonoCelular=request.json['telefonoCelular']
    cliente.miembroClub=request.json['miembroClub']
    cliente.direccionCliente=request.json['direccionCliente']
    cliente.pisoDeptoCliente=request.json['pisoDeptoCliente']
    cliente.codigoPostalCliente=request.json['codigoPostalCliente']
    cliente.localidadCliente=request.json['localidadCliente']
    cliente.provinciaCliente=request.json['provinciaCliente']

    db.session.commit()    # confirma el cambio
    return cliente_schema.jsonify(cliente)    # y retorna un json con el cliente



# Rutas para Item (similar a Cliente)
# ...

@app.route('/item',methods=['GET'])
def get_Items():
    all_items=Item.query.all()         # el metodo query.all() lo hereda de db.Model
    result=items_schema.dump(all_items)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla


@app.route('/item/<itemId>',methods=['GET'])
def get_item(itemId):
    item=Item.query.get(itemId)
    return item_schema.jsonify(item)   # retorna el JSON de un item recibido como parametro


@app.route('/item/<itemId>',methods=['DELETE'])
def delete_item(itemId):
    item=Item.query.get(itemId)
    db.session.delete(item)
    db.session.commit()                     # confirma el delete
    return item_schema.jsonify(item) # me devuelve un json con el registro eliminado


@app.route('/item', methods=['POST']) # crea ruta o endpoint
def create_item():
    #print(request.json)  # request.json contiene el json que envio el cliente

    nombreItem=request.json['nombreItem']
    descripcionItem=request.json['descripcionItem']
    fotoItem=request.json['fotoItem']
    precioItem=request.json['precioItem']
    stockItem=request.json['stockItem']
    precioClubItem=request.json['precioClubItem']
    
    new_item=Item(nombreItem,descripcionItem,fotoItem,precioItem,stockItem,precioClubItem)
    db.session.add(new_item)
    db.session.commit() # confirma el alta
    return item_schema.jsonify(new_item)


@app.route('/item/<itemId>' ,methods=['PUT'])
def update_producto(itemId):
    item=Item.query.get(itemId)

    item.nombreItem=request.json['nombreItem']
    item.descripcionItem=request.json['descripcionItem']
    item.fotoItem=request.json['fotoItem']
    item.precioItem=request.json['precioItem']
    item.stockItem=request.json['stockItem']
    item.precioClubItem=request.json['precioClubItem']


    db.session.commit()    # confirma el cambio
    return item_schema.jsonify(item)    # y retorna un json con el producto





# Rutas para Pedido (similar a Cliente)
# ...

@app.route('/pedido',methods=['GET'])
def get_Pedidos():
    all_pedidos=Pedido.query.all()         # el metodo query.all() lo hereda de db.Model
    result=pedidos_schema.dump(all_pedidos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla


@app.route('/productos/<productoId>',methods=['GET'])
def get_producto(productoId):
    producto=Producto.query.get(productoId)
    return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro


@app.route('/productos/<productoId>',methods=['DELETE'])
def delete_producto(productoId):
    producto=Producto.query.get(productoId)
    db.session.delete(producto)
    db.session.commit()                     # confirma el delete
    return producto_schema.jsonify(producto) # me devuelve un json con el registro eliminado


@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente

    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    fotoTarjeta=request.json['fotoTarjeta']
    precio=request.json['precio']
    stock=request.json['stock']
    precioClub=request.json['precioClub']
    fotoTarjetaOfertaClub=request.json['fotoTarjetaOfertaClub']
    fotoCaruselOfertaClub=request.json['fotoCaruselOfertaClub']
    fotoDestacado=request.json['fotoDestacado']

    new_producto=Producto(nombre,descripcion,fotoTarjeta,precio,stock,precioClub,fotoTarjetaOfertaClub,fotoCaruselOfertaClub,fotoDestacado)
    db.session.add(new_producto)
    db.session.commit() # confirma el alta
    return producto_schema.jsonify(new_producto)


@app.route('/productos/<productId>' ,methods=['PUT'])
def update_producto(productId):
    producto=Producto.query.get(productId)

    producto.nombre=request.json['nombre']
    producto.descripcion=request.json['descripcion']
    producto.fotoTarjeta=request.json['fotoTarjeta']
    producto.precio=request.json['precio']
    producto.stock=request.json['stock']
    producto.precioClub=request.json['precioClub']
    producto.fotoTarjetaOfertaClub=request.json['fotoTarjetaOfertaClub']
    producto.fotoCaruselOfertaClub=request.json['fotoCaruselOfertaClub']
    producto.fotoDestacado=request.json['fotoDestacado']

    db.session.commit()    # confirma el cambio
    return producto_schema.jsonify(producto)    # y retorna un json con el producto





class Pedido(db.Model):
    pedidoId = db.Column(db.Integer, primary_key=True)
    usuarioComprador = db.Column(db.String(20), db.ForeignKey('cliente.clienteId'))
    total = db.Column(db.Float)
    envio = db.Column(db.String(50))
    formaPago = db.Column(db.String(50))

    # Lista de ítems asociados al pedido (relación con Item)
    items = db.relationship('Item', backref='pedido', lazy=True)




# Rutas para Producto (similar a Cliente)
# ...

@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla


@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro


@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()                     # confirma el delete
    return producto_schema.jsonify(producto) # me devuelve un json con el registro eliminado


@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente

    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    fotoTarjeta=request.json['fotoTarjeta']
    precio=request.json['precio']
    stock=request.json['stock']
    precioClub=request.json['precioClub']
    fotoTarjetaOfertaClub=request.json['fotoTarjetaOfertaClub']
    fotoCaruselOfertaClub=request.json['fotoCaruselOfertaClub']
    fotoDestacado=request.json['fotoDestacado']

    new_producto=Producto(nombre,descripcion,fotoTarjeta,precio,stock,precioClub,fotoTarjetaOfertaClub,fotoCaruselOfertaClub,fotoDestacado)
    db.session.add(new_producto)
    db.session.commit() # confirma el alta
    return producto_schema.jsonify(new_producto)


@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)

    producto.nombre=request.json['nombre']
    producto.descripcion=request.json['descripcion']
    producto.fotoTarjeta=request.json['fotoTarjeta']
    producto.precio=request.json['precio']
    producto.stock=request.json['stock']
    producto.precioClub=request.json['precioClub']
    producto.fotoTarjetaOfertaClub=request.json['fotoTarjetaOfertaClub']
    producto.fotoCaruselOfertaClub=request.json['fotoCaruselOfertaClub']
    producto.fotoDestacado=request.json['fotoDestacado']

    db.session.commit()    # confirma el cambio
    return producto_schema.jsonify(producto)    # y retorna un json con el producto


# Punto de entrada de la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
