// Código Vue
const { createApp } = Vue;

createApp({
  data() {
    return {
      productos: [],
      productosAleatorios: [],
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
    truncateText(text, maxLength) {
      if (text.length <= maxLength) {
        return text;
      }
      const truncatedText = text.substring(0, maxLength) + '... <a href="#">Ver más</a>';
      return truncatedText;
    },
    fetchData(url) {
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.productos = data;
          // Obtener dos productos aleatorios
          this.productosAleatorios = this.obtenerProductosAleatorios(data, 2);
          console.log("Productos aleatorios:", this.productosAleatorios); // Para saber si los carga
          this.cargando = false;
          console.log("JSON data loaded successfully");

          // Llamada a la función para actualizar las tarjetas
          this.actualizarTarjetas(this.productosAleatorios);
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
        .then(res => res.text()) // o tambioen puede ser res.json()
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
          window.location.href = "./productos.html";  // recarga productos.html
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
    verProducto(producto) {
      const productId = producto.id; // Reemplaza 'id' con el nombre real de la propiedad del ID
      window.location.href = `producto-detalle.html?id=${productId}`;
    },
    actualizarTarjetas(productos) {
      console.log("Productos recibidos en actualizarTarjetas:", productos);

      // ... (código anterior)

      // Actualizar la primera tarjeta
      const tarjeta1 = document.getElementById('ofertas-sidebar');
      if (productos.length > 0) {
        tarjeta1.innerHTML = `
          <div class="producto-tarjeta">
            <h3>${productos[0].nombreProducto}</h3>
            <img src="${productos[0].fotoTarjetaProducto}" alt="${productos[0].nombreProducto}" class="imagen-tarjeta">
            <p>${this.truncateText(productos[0].descripcionProducto, 50)}</p>
            <a href="#">Ver más</a>
            <p>Valor: $ ${productos[0].precioClubProducto}</p>
            <p>Stock: ${productos[0].stockProducto} unidades disponibles</p>
            <!-- Otros elementos según sea necesario -->
          </div>
        `;
      } else {
        // Si no hay productos, limpiar la tarjeta
        tarjeta1.innerHTML = '';
      }

      // Actualizar la segunda tarjeta
      const tarjeta2 = document.getElementById('ofertas-sidebar2');
      if (productos.length > 1) {
        tarjeta2.innerHTML = `
          <div class="producto-tarjeta">
            <h3>${productos[1].nombreProducto}</h3>
            <img src="${productos[1].fotoTarjetaProducto}" alt="${productos[1].nombreProducto}" class="imagen-tarjeta">
            <p>${this.truncateText(productos[1].descripcionProducto, 50)}</p>
            <a href="#">Ver más</a>
            <p>Valor: $ ${productos[1].precioClubProducto}</p>
            <p>Stock: ${productos[1].stockProducto} unidades disponibles</p>
            <!-- Otros elementos según sea necesario -->
          </div>
        `;
      } else {
        // Si no hay suficientes productos, limpiar la tarjeta
        tarjeta2.innerHTML = '';
      }
    },
  },
  created() {
    this.fetchData(this.url);
    console.log("Component created successfully");
  },
}).mount('#tienda');