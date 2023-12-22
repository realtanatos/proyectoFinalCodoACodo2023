const { createApp } = Vue;

createApp({
  data() {
    return {
      productos: [],
      productosAleatorios: [],
      // URL for fetching and storing data
      url: 'https://thanathosar.pythonanywhere.com/productos',
      error: false,
      cargando: true,
      /* Attributes for storing form values */
      nombre: "",
      descripcion: "",
      fotoTarjeta: "",
      precio: 0,
      stock: 0,
      precioClub: 0,
      fotoTarjetaOfertaClub: "",
      fotoCaruselOfertaClub: "",
      fotoDestacado: "",
    };
  },
  methods: {
    fetchData(url) {
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.productos = data;
          // Obtener dos productos aleatorios
          this.productosAleatorios = this.obtenerProductosAleatorios(data, 2);
          this.cargando = false;
          console.log("JSON data loaded successfully");
        })
        .catch(err => {
          console.error('Error fetching data:', err);
          this.error = true;
          console.log("Error in fetchData from the database in productos.js");
        });
    },
    eliminar(id) {
      const url = `${this.url}/${id}`;
      var options = {
        method: 'DELETE',
      };
      fetch(url, options)
        .then(res => res.text()) // or res.json()
        .then(res => {
          alert('Registro Eliminado');
          location.reload(); // reloads the JSON after deleting the record
        })
        .catch(error => {
          console.error('Error deleting record:', error);
        });
    },
    grabar() {
      let producto = {
        nombreProducto: this.nombre,
        descripcionProducto: this.descripcion,
        fotoTarjetaProducto: this.fotoTarjeta,
        precioProducto: this.precio,
        stockProducto: this.stock,
        precioClubProducto: this.precioClub,
        fotoTarjetaOfertaClubProducto: this.fotoTarjetaOfertaClub,
        fotoCaruselOfertaClubProducto: this.fotoCaruselOfertaClub,
        fotoDestacadoProducto: this.fotoDestacado,
      };

      var options = {
        body: JSON.stringify(producto),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow',
      };

      fetch(this.url, options)
        .then(() => {
          alert("Registro grabado");
          window.location.href = "./productos.html";  // reloads productos.html
        })
        .catch(err => {
          console.error('Error saving record:', err);
          alert("Error al Grabar");  // displays an error message
        });
    },
    realizarBusqueda() {
      alert("El buscador se implementará pronto");
      // Puedes realizar otras acciones relacionadas con la búsqueda aquí
    },
    obtenerProductosAleatorios(productos, cantidad) {
      const productosAleatorios = [];
      const totalProductos = productos.length;

      // Obtener índices únicos al azar
      const indicesAleatorios = [];
      while (indicesAleatorios.length < cantidad) {
        const indice = Math.floor(Math.random() * totalProductos);
        if (!indicesAleatorios.includes(indice)) {
          indicesAleatorios.push(indice);
        }
      }

      // Obtener los productos correspondientes a los índices
      indicesAleatorios.forEach((indice) => {
        productosAleatorios.push(productos[indice]);
      });

      return productosAleatorios;
    },
  },
  created() {
    this.fetchData(this.url);
    console.log("Component created successfully");
  },
}).mount('#tienda');

// Función para actualizar el contenido de las tarjetas en el HTML
function actualizarTarjetas(productos) {
  // Actualizar la primera tarjeta
  const tarjeta1 = document.getElementById('ofertas-sidebar');
  if (productos.length > 0) {
    tarjeta1.innerHTML = `
      <h3>${productos[0].nombreProducto}</h3>
      <p>${productos[0].descripcionProducto}</p>
      <!-- Otros elementos según sea necesario -->
    `;
  }

  // Actualizar la segunda tarjeta
  const tarjeta2 = document.getElementById('ofertas-sidebar2');
  if (productos.length > 1) {
    tarjeta2.innerHTML = `
      <h3>${productos[1].nombreProducto}</h3>
      <p>${productos[1].descripcionProducto}</p>
      <!-- Otros elementos según sea necesario -->
    `;
  }
}

// Llamada a la función para actualizar las tarjetas
actualizarTarjetas([]);