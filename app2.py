from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os



app = Flask(__name__)
cors = CORS(app, resources={
    r"/api/*": {
        "origins": ["https://saraza-wine-club.netlify.app/", "https://saraza-backend.netlify.app/"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"],
        "expose_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True,
        "max_age": 3600,
    },
})

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
    telefonoFijo =  db.Column(db.String(20))
    telefonoCelular =  db.Column(db.String(20))
    miembroClub = db.Column(db.Boolean, default=False)
    direccionCliente = db.Column(db.String(200))
    pisoDeptoCliente = db.Column(db.String(50))
    codigoPostalCliente = db.Column(db.String(20))
    localidadCliente = db.Column(db.String(50))
    provinciaCliente = db.Column(db.String(50))

    # Asignación de valores con el
    # Constructor de la clase
    def __init__(self, nombreUsuario, nombreApellido, email, clave, telefonoFijo, telefonoCelular, miembroClub,
                 direccionCliente, pisoDeptoCliente, codigoPostalCliente, localidadCliente, provinciaCliente):
        self.nombreUsuario = nombreUsuario
        self.nombreApellido = nombreApellido
        self.email = email
        self.clave = clave
        self.telefonoFijo = telefonoFijo
        self.telefonoCelular = telefonoCelular
        self.miembroClub = miembroClub
        self.direccionCliente = direccionCliente
        self.pisoDeptoCliente = pisoDeptoCliente
        self.codigoPostalCliente = codigoPostalCliente
        self.localidadCliente = localidadCliente
        self.provinciaCliente = provinciaCliente

    def __str__(self):
        return f"Cliente ID: {self.cliente_id} - Nombre: {self.nombre} - Email: {self.email} - Teléfono: {self.telefono}"


class Producto(db.Model):
    productoId = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(100))
    descripcionProducto = db.Column(db.String(300))
    fotoTarjetaProducto = db.Column(db.String(200))
    precioProducto = db.Column(db.Float)
    stockProducto = db.Column(db.Integer)
    precioClubProducto = db.Column(db.Float)
    fotoTarjetaOfertaClubProducto = db.Column(db.String(200))
    fotoCaruselOfertaClubProducto = db.Column(db.String(200))
    fotoDestacadoProducto = db.Column(db.String(100))

    # Constructor de la clase
    def __init__(self, nombreProducto, descripcionProducto, fotoTarjetaProducto, precioProducto, stockProducto, precioClubProducto, fotoTarjetaOfertaClubProducto,
                 fotoCaruselOfertaClubProducto, fotoDestacadoProducto):
        self.nombreProducto = nombreProducto
        self.descripcionProducto = descripcionProducto
        self.fotoTarjetaProducto = fotoTarjetaProducto
        self.precioProducto = precioProducto
        self.stockProducto = stockProducto
        self.precioClubProducto = precioClubProducto
        self.fotoTarjetaOfertaClubProducto = fotoTarjetaOfertaClubProducto
        self.fotoCaruselOfertaClubProducto = fotoCaruselOfertaClubProducto
        self.fotoDestacadoProducto = fotoDestacadoProducto


class Pedido(db.Model):
    pedidoId = db.Column(db.Integer, primary_key=True)
    usuarioComprador = db.Column(db.String(20), db.ForeignKey('cliente.nombreUsuario'))
    nombreApellidoComprador = db.Column(db.String(20), db.ForeignKey('cliente.nombreApellido'))
    items = db.relationship('PedidoItems', backref='pedido', lazy='dynamic')
    totalAPagar = db.Column(db.Float)
    direccionEnvio = db.relationship('Cliente', backref='direccionCliente')
    pisoDeptoEnvio = db.relationship('Cliente', backref='pisoDeptoCliente')
    codigoPostalEnvio = db.relationship('Cliente', backref='codigoPostalCliente')
    localidadEnvio = db.relationship('Cliente', backref='localidadCliente')
    provinciaEnvio = db.relationship('Cliente', backref='provinciaCliente')
    formaPago = db.Column(db.String(20))

    def __init__(self, usuarioComprador, nombreApellidoComprador, totalAPagar, direccionEnvio, pisoDeptoEnvio, codigoPostalEnvio, localidadEnvio, provinciaEnvio, formaPago, items=None):
        self.usuarioComprador = usuarioComprador
        self.nombreApellidoComprador = nombreApellidoComprador
        self.totalAPagar = totalAPagar
        self.direccionEnvio = direccionEnvio
        self.pisoDeptoEnvio = pisoDeptoEnvio
        self.codigoPostalEnvio = codigoPostalEnvio
        self.localidadEnvio = localidadEnvio
        self.provinciaEnvio = provinciaEnvio
        self.formaPago = formaPago

    def imprimirFactura(self):
        items_info = [
            f"Producto: {item.nombreItemsPedidos}, Cantidad: {item.cantidadItemsPedidos}, Precio Pedido: {item.precioProductoPedido}, Precio Descuento Pedido: {item.precioProductoDescuentoPedido}, Subtotal (con descuento): {item.cantidadItemsPedidos * item.precioProductoDescuentoPedido}, Subtotal (sin descuento): {item.cantidadItemsPedidos * item.precioProductoPedido}"
            for item in self.items
        ]
        subtotal_con_descuento = sum(item.cantidadItemsPedidos * item.precioProductoDescuentoPedido for item in self.items)
        subtotal_sin_descuento = sum(item.cantidadItemsPedidos * item.precioProductoPedido for item in self.items)

        return f"Pedido ID: {self.pedidoId}\n\nDatos del Cliente:\nUsuario: {self.usuarioComprador}\nNombre y Apellido: {self.nombreApellidoComprador}\n\nDetalle del Pedido:\n{items_info}\n\nTotal a Pagar (con descuento): {subtotal_con_descuento}\nTotal a Pagar (sin descuento): {subtotal_sin_descuento}\n\nForma de Pago: {self.formaPago}\n\nDatos de Envío:\nDirección: {self.direccionEnvio}\nPiso/Depto: {self.pisoDeptoEnvio}\nCódigo Postal: {self.codigoPostalEnvio}\nLocalidad: {self.localidadEnvio}\nProvincia: {self.provinciaEnvio}"

    def __str__(self):
        return self.imprimirFactura()


class PedidoItems(db.Model):
    pedidoItemsId = db.Column(db.Integer, primary_key=True)
    pedidoNroOrden = db.Column(db.Integer, db.ForeignKey('pedido.pedidoId'))
    productoPedidoItems = db.Column(db.Integer, db.ForeignKey('producto.productoId'))
    nombreItemsPedidos = db.Column(db.String, db.ForeignKey('producto.nombre'))
    cantidadItemsPedidos = db.Column(db.Integer)
    precioProductoPedido = db.Column(db.Float, db.ForeignKey('producto.precio'))
    precioProductoDescuentoPedido = db.Column(db.Float, db.ForeignKey('producto.precioClub'))
    producto = db.relationship('Producto', foreign_keys=[productoPedidoItems])

    def __init__(self, pedidoNroOrden, productoPedidoItems, nombreItemsPedidos, cantidadItemsPedidos, precioProductoPedido, precioProductoDescuentoPedido):
        self.pedidoNroOrden = pedidoNroOrden
        self.productoPedidoItems = productoPedidoItems
        self.nombreItemsPedidos = nombreItemsPedidos
        self.cantidadItemsPedidos = cantidadItemsPedidos
        self.precioProductoPedido = precioProductoPedido
        self.precioProductoDescuentoPedido = precioProductoDescuentoPedido

    def __str__(self):
        return f"Producto: {self.nombreItemsPedidos}, Cantidad: {self.cantidadItemsPedidos}, Precio Pedido: {self.precioProductoPedido}, Precio Descuento Pedido: {self.precioProductoDescuentoPedido}, Subtotal (con descuento): {self.cantidadItemsPedidos * self.precioProductoDescuentoPedido}, Subtotal (sin descuento): {self.cantidadItemsPedidos * self.precioProductoPedido}"


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
        fields = ('pedidoId', 'usuarioComprador', 'items', 'totalAPagar', 'direccionEnvio', 'pisoDeptoEnvio', 'codigoPostalEnvio', 'localidadEnvio', 'provinciaEnvio', 'formaPago')

pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)

class PedidoItemsSchema(ma.Schema):
    class Meta:
        fields = ('pedidoItemsId', 'pedidoNroOrden', 'productoPedidoItems', 'nombreItemsPedidos', 'cantidadItemsPedidos', 'precioProductoPedido', 'precioProductoDescuentoPedido')

pedido_item_schema = PedidoItemsSchema()
pedido_items_schema = PedidoItemsSchema(many=True)


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
def get_pedidos():
    all_pedidos = Pedido.query.all()
    result = pedidos_schema.dump(all_pedidos)
    return jsonify(result)

@app.route('/pedidos/<int:pedidoId>', methods=['GET'])
def get_pedido(pedidoId):
    pedido = Pedido.query.get(pedidoId)
    return pedido_schema.jsonify(pedido)

@app.route('/pedidos', methods=['POST'])
def create_pedido():
    data = request.json
    nuevo_pedido = Pedido(usuarioComprador=data['usuarioComprador'], totalAPagar=data['totalAPagar'], formaPago=data['formaPago'])
    db.session.add(nuevo_pedido)
    
    # Añadir items al pedido si se proporcionan
    if 'items' in data:
        for item in data['items']:
            pedido_item = PedidoItems(pedidoNroOrden=nuevo_pedido.pedidoId, productoPedidoItems=item['productoPedidoItems'], cantidadItemsPedidos=item['cantidadItemsPedidos'])
            db.session.add(pedido_item)

    # Añadir dirección de envío si se proporciona
    if 'direccionEnvio' in data:
        nuevo_pedido.direccionEnvio = data['direccionEnvio']

    db.session.commit()
    return pedido_schema.jsonify(nuevo_pedido)

# Ruta para actualizar un pedido
@app.route('/pedidos/<int:pedidoId>', methods=['PUT'])
def update_pedido(pedidoId):
    pedido = Pedido.query.get(pedidoId)
    
    data = request.json
    pedido.usuarioComprador = data.get('usuarioComprador', pedido.usuarioComprador)
    pedido.totalAPagar = data.get('totalAPagar', pedido.totalAPagar)
    pedido.direccionEnvio = data.get('direccionEnvio', pedido.direccionEnvio)
    pedido.pisoDeptoEnvio = data.get('pisoDeptoEnvio', pedido.pisoDeptoEnvio)
    pedido.codigoPostalEnvio = data.get('codigoPostalEnvio', pedido.codigoPostalEnvio)
    pedido.localidadEnvio = data.get('localidadEnvio', pedido.localidadEnvio)
    pedido.provinciaEnvio = data.get('provinciaEnvio', pedido.provinciaEnvio)
    pedido.formaPago = data.get('formaPago', pedido.formaPago)

    # Guardar los cambios en la base de datos
    db.session.commit()

    return jsonify({'message': 'Pedido actualizado correctamente'})

# Ruta para eliminar un pedido
@app.route('/pedidos/<int:pedidoId>', methods=['DELETE'])
def delete_pedido(pedidoId):
    pedido = Pedido.query.get(pedidoId)
    db.session.delete(pedido)
    db.session.commit()
    
    return jsonify({'message': 'Pedido eliminado correctamente'})



# Ruta para obtener todos los PEDIDOITEMS de pedido
@app.route('/pedidoitems', methods=['GET'])
def get_pedido_items():
    all_items = PedidoItems.query.all()
    result = pedido_items_schema.dump(all_items)
    return jsonify(result)

# Ruta para obtener un item de pedido por su ID
@app.route('/pedidoitems/<int:pedidoItemsId>', methods=['GET'])
def get_pedido_item(pedidoItemsId):
    item = PedidoItems.query.get(pedidoItemsId)
    return pedido_item_schema.jsonify(item)

# Ruta para agregar un nuevo item de pedido
@app.route('/pedidoitems', methods=['POST'])
def add_pedido_item():
    pedidoNroOrden = request.json['pedidoNroOrden']
    productoPedidoItems = request.json['productoPedidoItems']
    nombreItemsPedidos = request.json['nombreItemsPedidos']
    cantidadItemsPedidos = request.json['cantidadItemsPedidos']
    precioProductoPedido = request.json['precioProductoPedido']
    precioProductoDescuentoPedido = request.json['precioProductoDescuentoPedido']

    new_item = PedidoItems(pedidoNroOrden=pedidoNroOrden, productoPedidoItems=productoPedidoItems, nombreItemsPedidos=nombreItemsPedidos, cantidadItemsPedidos=cantidadItemsPedidos, precioProductoPedido=precioProductoPedido, precioProductoDescuentoPedido=precioProductoDescuentoPedido)
    db.session.add(new_item)
    db.session.commit()

    return pedido_item_schema.jsonify(new_item)

# Ruta para actualizar un item de pedido
@app.route('/pedidoitems/<int:pedidoItemsId>', methods=['PUT'])
def update_pedido_item(pedidoItemsId):
    item = PedidoItems.query.get(pedidoItemsId)

    item.pedidoNroOrden = request.json.get('pedidoNroOrden', item.pedidoNroOrden)
    item.productoPedidoItems = request.json.get('productoPedidoItems', item.productoPedidoItems)
    item.nombreItemsPedidos = request.json.get('nombreItemsPedidos', item.nombreItemsPedidos)
    item.cantidadItemsPedidos = request.json.get('cantidadItemsPedidos', item.cantidadItemsPedidos)
    item.precioProductoPedido = request.json.get('precioProductoPedido', item.precioProductoPedido)
    item.precioProductoDescuentoPedido = request.json.get('precioProductoDescuentoPedido', item.precioProductoDescuentoPedido)

    db.session.commit()

    return pedido_item_schema.jsonify(item)

# Ruta para eliminar un item de pedido
@app.route('/pedidoitems/<int:pedidoItemsId>', methods=['DELETE'])
def delete_pedido_item(pedidoItemsId):
    item = PedidoItems.query.get(pedidoItemsId)
    db.session.delete(item)
    db.session.commit()

    return jsonify({'message': 'Item de pedido eliminado correctamente'})




# Punto de entrada de la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
