from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://TallerInfoTecno:prueba1234@TallerInfoTecno.mysql.pythonanywhere-services.com/TallerInfoTecno$default'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/proyecto'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Modelos
class Cliente(db.Model):
    clienteId = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(20), unique=True, nullable=False)
    nombreApellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    clave = db.Column(db.String(20), nullable=False)
    telefonoFijo = db.Column(db.String(20))
    telefonoCelular = db.Column(db.String(20))
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
        return f"Cliente ID: {self.clienteId} - Nombre: {self.nombreApellido} - Email: {self.email} - Teléfono Celular: {self.telefonoCelular}"


class Producto(db.Model):
    productoId = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(100), nullable=False)
    descripcionProducto = db.Column(db.String(300))
    fotoTarjetaProducto = db.Column(db.String(200))
    precioProducto = db.Column(db.Float, nullable=False)
    stockProducto = db.Column(db.Integer, nullable=False)
    precioClubProducto = db.Column(db.Float, nullable=False)
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
    usuarioComprador = db.Column(db.String(20), nullable=False)
    nombreApellidoComprador = db.Column(db.String(20), nullable=False)
    totalAPagar = db.Column(db.Float, nullable=False)
    formaPago = db.Column(db.String(20), nullable=False)
    direccionEnvio = db.Column(db.String(200))
    pisoDeptoEnvio = db.Column(db.String(50))
    codigoPostalEnvio = db.Column(db.String(20))
    localidadEnvio = db.Column(db.String(50))
    provinciaEnvio = db.Column(db.String(50))
    items = db.relationship('PedidoItems', backref='pedido', lazy=True)


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
    pedidoNroOrden = db.Column(db.Integer, db.ForeignKey('pedido.pedidoId'), nullable=False)
    productoPedidoItems = db.Column(db.Integer, db.ForeignKey('producto.productoId'), nullable=False)
    nombreItemsPedidos = db.Column(db.String(100), nullable=False)
    cantidadItemsPedidos = db.Column(db.Integer, nullable=False)
    precioProductoPedido = db.Column(db.Float, nullable=False)
    precioProductoDescuentoPedido = db.Column(db.Float, nullable=False)
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
                  'miembroClub', 'direccionCliente', 'pisoDeptoCliente', 'codigoPostalCliente', 'localidadCliente', 'provinciaCliente')

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('productoId', 'nombreProducto', 'descripcionProducto', 'fotoTarjetaProducto', 'precioProducto', 'stockProducto', 'precioClubProducto',
                  'fotoTarjetaOfertaClubProducto', 'fotoCaruselOfertaClubProducto', 'fotoDestacadoProducto')

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
@app.route('/productos', methods=['GET'])
def get_productos():
    print("Se ha llamado a la ruta /productos")
    all_productos = Producto.query.all()
    result = productos_schema.dump(all_productos)
    return jsonify(result)
print("termino el llamado a la ruta /productos")

@app.route('/productos/<int:productoId>', methods=['GET'])
def get_producto(productoId):
    producto = Producto.query.get(productoId)
    return producto_schema.jsonify(producto)

@app.route('/productos', methods=['POST'])
def create_producto():
    data = request.json
    new_producto = Producto(**data)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

@app.route('/productos/<int:productoId>', methods=['PUT'])
def update_producto(productoId):
    producto = Producto.query.get(productoId)
    data = request.json
    for key, value in data.items():
        setattr(producto, key, value)
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/productos/<int:productoId>', methods=['DELETE'])
def delete_producto(productoId):
    producto = Producto.query.get(productoId)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)

# Rutas de CLIENTES para Cliente Web
@app.route('/clientes', methods=['GET'])
def get_clientes():
    all_clientes = Cliente.query.all()
    result = clientes_schema.dump(all_clientes)
    return jsonify(result)

@app.route('/clientes/<int:clienteId>', methods=['GET'])
def get_cliente(clienteId):
    cliente = Cliente.query.get(clienteId)
    return cliente_schema.jsonify(cliente)

@app.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.json
    new_cliente = Cliente(**data)
    db.session.add(new_cliente)
    db.session.commit()
    return cliente_schema.jsonify(new_cliente)

@app.route('/clientes/<int:clienteId>', methods=['PUT'])
def update_cliente(clienteId):
    cliente = Cliente.query.get(clienteId)
    data = request.json
    for key, value in data.items():
        setattr(cliente, key, value)
    db.session.commit()
    return cliente_schema.jsonify(cliente)

@app.route('/clientes/<int:clienteId>', methods=['DELETE'])
def delete_cliente(clienteId):
    cliente = Cliente.query.get(clienteId)
    db.session.delete(cliente)
    db.session.commit()
    return cliente_schema.jsonify(cliente)

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
        for item_data in data['items']:
            nuevo_item = PedidoItems(nombreItemsPedidos=item_data['nombreItemsPedidos'], cantidadItemsPedidos=item_data['cantidadItemsPedidos'])
            nuevo_pedido.items.append(nuevo_item)

    # Añadir dirección de envío si se proporciona
    if 'direccionEnvio' in data:
        nuevo_pedido.direccionEnvio = data['direccionEnvio']

    db.session.commit()
    return pedido_schema.jsonify(nuevo_pedido)

'''
después de agregar nuevo_pedido a la sesión (db.session.add(nuevo_pedido)), nos fijamos
si hay elementos en data['items']. Si hay elementos, se recorre cada uno y se crea
un nuevo objeto PedidoItems (nuevo_item). Luego, este nuevo ítem se agrega a la lista
de ítems del nuevo_pedido mediante nuevo_pedido.items.append(nuevo_item).

Al final agregamos la dirección de envío si está presente en los datos y mandamos los datos de la
sesión con db.session.commit().

Lo hacemos asi para que los items asociados al pedido esten todos correctos con el pedido antes
de confiormar el envio del pedido a la base de datos...


'''


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


# A very simple Flask Hello World app for you to get started with...


# Manejador de errores
@app.errorhandler(Exception)
def handle_error(e):
    app.logger.error(f"Error: {str(e)}")
    return jsonify(error=str(e)), 500


# A very simple Flask Hello World app for you to get started with...

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# Si este script es ejecutado, arranca la aplicación
if __name__ == '__main__':
    app.run(debug=True)
