from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os



app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
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
    telefonoFijo = db.Column(db.Integer)
    telefonoCelular = db.Column(db.Integer)
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


class Pedido(db.Model):
    pedidoId = db.Column(db.Integer, primary_key=True)
    usuarioComprador = db.Column(db.String(20), db.ForeignKey('cliente.clienteId'))

    # Relación con la clase Producto
    items = db.relationship('Producto', secondary='PedidoItem', backref='pedidos')

    total = db.Column(db.Float)
    direccionEnvio = db.relationship('Cliente', backref='direccionCliente')  # Relación con la clase Cliente
    pisoDeptoEnvio = db.relationship('Cliente', backref='pisoDeptoCliente')  # Relación con la clase Cliente
    codigoPostalEnvio = db.relationship('Cliente', backref='codigoPostalCliente')  # Relación con la clase Cliente
    localidadEnvio = db.relationship('Cliente', backref='localidadCliente')  # Relación con la clase Cliente
    provinciaEnvio = db.relationship('Cliente', backref='provinciaCliente')  # Relación con la clase Cliente
    formaPago = db.Column(db.String(20))

    def __init__(self, usuarioComprador, total, direccionEnvio, pisoDeptoEnvio,codigoPostalEnvio,localidadEnvio,provinciaEnvio,formaPago, items=None, direccionEnvio=None):
        self.usuarioComprador = usuarioComprador
        self.total = total
        self.direccionEnvio=direccionEnvio
        self.codigoPostalEnvio=codigoPostalEnvio
        self.localidadEnvio=localidadEnvio
        self.provinciaEnvio=provinciaEnvio
        self.formaPago = formaPago


class PedidoItem(db.Model):

# Aca voy a llamar a los parametros no con camelcase sino con _ para darme cuenta de que estoy haciendo referencia a la tabla de relaciones de pedidos entre productos y clientes
    pedidoItemId = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.pedidoId'))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    cantidad = db.Column(db.Integer)
    precioPedido = db.Column(db.Float, db.ForeignKey('producto.precio'))
    precioDescuentoPedido = db.Column(db.Float, db.ForeignKey('producto.precioClub'))

    # Relación para acceder al objeto Producto asociado y recuperar el precio
    producto = db.relationship('Producto', foreign_keys=[producto_id])

    def __init__(self, pedido_id, producto_id, cantidad, precioPedido, precioDescuentoPedido):
        self.pedido_id = pedido_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        # El precioPedido se recuperará automáticamente a través de la relación por eso no los inicializo
        # El precioDescuentoPedido se recuperará automáticamente a través de la relación por eso no los inicializo




# Creación de todas las tablas

with app.app_context():
    db.create_all()

# Esquemas
class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('clienteId', 'nombreUsuario', 'nombreApellido', 'email', 'clave', 'telefonoFijo', 'telefonoCelular',
                  'miembroClub', 'direccionEnvio', 'pisoDeptoEnvio', 'codigoPostalEnvio', 'localidadEnvio', 'provinciaEnvio')

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('productoId', 'nombre', 'descripcion', 'fotoTarjeta', 'precio', 'stock', 'precioClub',
                  'fotoTarjetaOfertaClub', 'fotoCaruselOfertaClub', 'fotoDestacado')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)


class PedidoSchema(ma.Schema):
    class Meta:
        fields = ('pedidoId', 'usuarioComprador', 'items', 'total', 'direccionEnvio', 'pisoDeptoEnvio', 'codigoPostalEnvio', 'localidadEnvio', 'provinciaEnvio', 'formaPago')

pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)

class PedidoItemSchema(ma.Schema):
    class Meta:
        fields = ('pedidoItemId', 'pedido_id', 'producto_id', 'cantidad', 'precioPedido', 'precioDescuentoPedido', 'producto')

pedido_item_schema = PedidoItemSchema()
pedido_items_schema = PedidoItemSchema(many=True)




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
def get_Clientes():
    all_clientes = Cliente.query.all()
    result = clientes_schema.dump(all_clientes)
    return jsonify(result)

@app.route('/clientes/<clienteId>', methods=['GET'])
def get_cliente(clienteId):
    cliente = Cliente.query.get(clienteId)
    return cliente_schema.jsonify(cliente)


@app.route('/clientes/<clienteId>',methods=['DELETE'])
def delete_cliente(clienteId):
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
    direccionEnvio=request.json['direccionEnvio']
    pisoDeptoEnvio=request.json['pisoDeptoEnvio']
    codigoPostalEnvio=request.json['codigoPostalEnvio']
    localidadEnvio=request.json['localidadEnvio']
    provinciaEnvio=request.json['provinciaEnvio']

    new_cliente = Cliente(nombreUsuario, nombreApellido, email, clave, telefonoFijo, telefonoCelular, miembroClub,
                          direccionEnvio, pisoDeptoEnvio, codigoPostalEnvio, localidadEnvio, provinciaEnvio)
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
    cliente.direccionEnvio=request.json['direccionEnvio']
    cliente.pisoDeptoEnvio=request.json['pisoDeptoEnvio']
    cliente.codigoPostalEnvio=request.json['codigoPostalEnvio']
    cliente.localidadEnvio=request.json['localidadEnvio']
    cliente.provinciaEnvio=request.json['provinciaEnvio']

    db.session.commit()    # confirma el cambio
    return cliente_schema.jsonify(cliente)    # y retorna un json con el cliente


# Rutas para PEDIDO
@app.route('/pedidos', methods=['GET'])
def get_Pedidos():
    all_pedidos = Pedido.query.all()
    result = pedidos_schema.dump(all_pedidos)
    return jsonify(result)

@app.route('/pedidos/<pedidoId>', methods=['GET'])
def get_pedido(pedidoId):
    pedido = Pedido.query.get(pedidoId)
    return pedido_schema.jsonify(pedido)

@app.route('/pedidos', methods=['POST'])
def create_pedido():
    data = request.json
    nuevo_pedido = Pedido(usuarioComprador=data['usuarioComprador'], total=data['total'], formaPago=data['formaPago'])
    db.session.add(nuevo_pedido)
    
    # Añadir items al pedido si se proporcionan
    if 'items' in data:
        for item in data['items']:
            pedido_item = PedidoItem(pedido_id=nuevo_pedido.pedidoId, producto_id=item['producto_id'], cantidad=item['cantidad'])
            db.session.add(pedido_item)

    # Añadir dirección de envío si se proporciona
    if 'direccionEnvio' in data:
        nuevo_pedido.direccionEnvio = data['direccionEnvio']

    db.session.commit()
    return pedido_schema.jsonify(nuevo_pedido)

# Ruta para actualizar un pedido
@app.route('/pedidos/<pedido_id>', methods=['PUT'])
def update_pedido(pedido_id):
    pedido = Pedido.query.get(pedido_id)
    
    # Actualizar los campos si están presentes en la solicitud
    pedido.usuarioComprador = request.json.get('usuarioComprador', pedido.usuarioComprador)
    pedido.total = request.json.get('total', pedido.total)
    pedido.direccionEnvio = request.json.get('direccionEnvio', pedido.direccionEnvio)
    pedido.pisoDeptoEnvio = request.json.get('pisoDeptoEnvio', pedido.pisoDeptoEnvio)
    pedido.codigoPostalEnvio = request.json.get('codigoPostalEnvio', pedido.codigoPostalEnvio)
    pedido.localidadEnvio = request.json.get('localidadEnvio', pedido.localidadEnvio)
    pedido.provinciaEnvio = request.json.get('provinciaEnvio', pedido.provinciaEnvio)
    pedido.formaPago = request.json.get('formaPago', pedido.formaPago)

    # Guardar los cambios en la base de datos
    db.session.commit()

    return jsonify({'message': 'Pedido actualizado correctamente'})

# Ruta para eliminar un pedido
@app.route('/pedidos/<pedido_id>', methods=['DELETE'])
def delete_pedido(pedido_id):
    pedido = Pedido.query.get(pedido_id)
    db.session.delete(pedido)
    db.session.commit()
    
    return jsonify({'message': 'Pedido eliminado correctamente'})



# Ruta para obtener todos los PEDIDOITEMS de pedido
@app.route('/pedidoitems', methods=['GET'])
def get_pedido_items():
    all_items = PedidoItem.query.all()
    result = pedido_items_schema.dump(all_items)
    return jsonify(result)

# Ruta para obtener un item de pedido por su ID
@app.route('/pedidoitems/<item_id>', methods=['GET'])
def get_pedido_item(item_id):
    item = PedidoItem.query.get(item_id)
    return pedido_item_schema.jsonify(item)

# Ruta para agregar un nuevo item de pedido
@app.route('/pedidoitems', methods=['POST'])
def add_pedido_item():
    pedido_id = request.json['pedido_id']
    producto_id = request.json['producto_id']
    cantidad = request.json['cantidad']

    new_item = PedidoItem(pedido_id=pedido_id, producto_id=producto_id, cantidad=cantidad)
    db.session.add(new_item)
    db.session.commit()

    return pedido_item_schema.jsonify(new_item)

# Ruta para actualizar un item de pedido
@app.route('/pedidoitems/<item_id>', methods=['PUT'])
def update_pedido_item(item_id):
    item = PedidoItem.query.get(item_id)

    item.pedido_id = request.json.get('pedido_id', item.pedido_id)
    item.producto_id = request.json.get('producto_id', item.producto_id)
    item.cantidad = request.json.get('cantidad', item.cantidad)

    db.session.commit()

    return pedido_item_schema.jsonify(item)

# Ruta para eliminar un item de pedido
@app.route('/pedidoitems/<item_id>', methods=['DELETE'])
def delete_pedido_item(item_id):
    item = PedidoItem.query.get(item_id)
    db.session.delete(item)
    db.session.commit()

    return jsonify({'message': 'Item de pedido eliminado correctamente'})




# Punto de entrada de la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
