const { createApp } = Vue;

createApp({
  data() {
    return {
      pedidos: [],
      url: 'https://thanathosar.pythonanywhere.com/pedidos',
      error: false,
      cargando: true,
      // Otros atributos necesarios para el formulario de pedido
      nuevoPedido: {
        // Inicializa aquí los campos del nuevo pedido
        usuarioComprador: '',
        nombreApellidoComprador: '',
        totalAPagar: 0,
        direccionEnvio: '',
        pisoDeptoEnvio: '',
        codigoPostalEnvio: '',
        localidadEnvio: '',
        provinciaEnvio: '',
        formaPago: '',
        // Otros campos del pedido
      },
    };
  },
  methods: {
    fetchData(url) {
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.pedidos = data;
          this.cargando = false;
          console.log('Datos de pedidos cargados');
        })
        .catch(err => {
          console.error(err);
          this.error = true;
          console.log('Error al cargar datos de pedidos');
        });
    },
      // Método para crear un nuevo pedido
  crearPedido() {
    // Validar que se haya ingresado un usuario comprador
    if (!this.nuevoPedido.usuarioComprador) {
        alert('Por favor, ingrese un usuario comprador.');
        return;
      }
  
      // Validar que se haya ingresado un total a pagar válido
      if (isNaN(this.nuevoPedido.totalAPagar) || this.nuevoPedido.totalAPagar <= 0) {
        alert('Por favor, ingrese un total a pagar válido.');
        return;
      }
  

    // Enviar el pedido al serverr con POST
    fetch(this.url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(this.nuevoPedido),
    })
      .then(response => response.json())
      .then(data => {
        // Vemos si se creo ok
        console.log('Pedido creado:', data);

        // Limpiamos el formulario después
        this.nuevoPedido = {
          usuarioComprador: '',
          nombreApellidoComprador: '',
          totalAPagar: 0,
          direccionEnvio: '',
          pisoDeptoEnvio: '',
          codigoPostalEnvio: '',
          localidadEnvio: '',
          provinciaEnvio: '',
          formaPago: '',
          campoEjemplo1: '',
          campoEjemplo2: '',
          campoEjemplo3: '',
        };
      })
      .catch(error => {
        // Con esto manejo errores que sucedan durante la creación del pedido
        console.error('Error al crear el pedido:', error);
      });
    },
    
    eliminarPedido(pedidoId) {
      const url = `${this.url}/${pedidoId}`;
      var options = {
        method: 'DELETE',
      };
      fetch(url, options)
        .then(res => res.text())
        .then(res => {
          alert('Pedido eliminado correctamente');
          this.fetchData(this.url); // Recargar la lista de pedidos
        })
        .catch(err => {
          console.error(err);
          alert('Error al eliminar pedido');
        });
    },
    guardarPedido() {
      var options = {
        body: JSON.stringify(this.nuevoPedido),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      };
      fetch(this.url, options)
        .then(response => response.json())
        .then(data => {
          alert('Pedido creado correctamente');
          this.fetchData(this.url); // Recargar la lista de pedidos
        })
        .catch(err => {
          console.error(err);
          alert('Error al crear pedido');
        });
    },

    // Actualizamos un pedido
    actualizarPedido(pedidoId) {
      const url = `${this.url}/${pedidoId}`;
      var options = {
        body: JSON.stringify(this.nuevoPedido),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
      };
      fetch(url, options)
        .then(response => response.json())
        .then(data => {
          alert('Pedido actualizado correctamente');
          this.fetchData(this.url); // Recargar la lista de pedidos
        })
        .catch(err => {
          console.error(err);
          alert('Error al actualizar pedido');
        });
    },
  },
  created() {
    this.fetchData(this.url);
    console.log('Componente creado');
  },
}).mount('#app');
