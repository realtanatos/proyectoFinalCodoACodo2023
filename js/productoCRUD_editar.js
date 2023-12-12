console.log(location.search)     // lee los argumentos pasados a este formulario
var id=location.search.substr(4)  // producto_update.html?id=1
console.log(id)
const { createApp } = Vue
  createApp({
    data() {
      return {
        id:0,
        nombre:"",
        descripcion:"",
        fotoTarjeta:"",
        precio:0,
        stock:0,
        precioClub:0,
        fotoTarjetaOfertaClub:"",
        fotoCaruselOfertaClub:"",
        fotoDestacado:"",
        url:'https://thanathosar.pythonanywhere.com/productos/'+id,
        imagen:"",
       }  
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.id=data.productoId,
                    this.nombre=data.nombreProducto,
                    this.descripcion=data.descripcionProducto,
                    this.fotoTarjeta=data.fotoTarjetaProducto,
                    this.precio=data.precioProducto,
                    this.stock=data.stockProducto,
                    this.precioClub=data.precioClubProducto,
                    this.fotoTarjetaOfertaClub=data.fotoTarjetaOfertaClubProducto,
                    this.fotoCaruselOfertaClub=data.fotoCaruselOfertaClubProducto,
                    this.fotoDestacado=data.fotoDestacadoProducto

                })
                .catch(err => {
                    console.error(err);
                    this.error=true;
                    console.log("Error en el fetchData de la base de datos en producto_editar.js");                  
                })
        },
        modificar() {
            let producto = {
                nombreProducto: this.nombre,
                descripcionProducto: this.descripcion,
                fotoTarjetaProducto: this.fotoTarjeta,
                precioProducto: this.precio,
                stockProducto: this.stock,
                precioClubProducto: this.precioClub,
                fotoTarjetaOfertaClubProducto: this.fotoTarjetaOfertaClub,
                fotoCaruselOfertaClubProducto: this.fotoCaruselOfertaClub,
                fotoDestacadoProducto: this.fotoDestacado
              };
            var options = {
                body: JSON.stringify(producto),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    console.log(producto)
                    alert("Registro modificado")
                    window.location.href = "./productos.html"; // navega a productos.html          
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })      
        }
    },
    created() {
        this.fetchData(this.url)
    },
  }).mount('#app')