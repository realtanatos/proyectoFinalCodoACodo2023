const { createApp } = Vue;

createApp({
  data() {
    return {
      productos: [],
      // URL para el fetching y storing data
      url: 'https://thanathosar.pythonanywhere.com/productos',
      error: false,
      cargando: true,
      /* Atributos para guardar los valores */
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
      console.log("Fetching data from:", url);
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.productos = data;
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
        .then(res => res.text())
        .then(res => {
          alert('Registro Eliminado');
          location.reload(); // recarga el JSON despues de borrar el registro
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
          window.location.href = "./productosCRUD.html";  // recarga productos.html
        })
        .catch(err => {
          console.error('Error saving record:', err);
          alert("Error al Grabar");  // Mostrar mensaje de error
        });
    },
    realizarBusqueda() {
      alert("El buscador se implementará pronto");
      // Otras acciones relacionadas con la búsqueda, se ponen aquí
    },
  },
  created() {
    this.fetchData(this.url);
    console.log("Component created successfully");
  },
}).mount('#tienda');
