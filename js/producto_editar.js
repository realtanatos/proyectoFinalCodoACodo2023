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
       }  
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.id=data.id
                    this.nombre=data.nombre,
                    this.descripcion=data.descripcion,
                    this,fotoTarjeta=data.fotoTarjeta,
                    this.precio=data.precio,
                    this.stock=data.stock,
                    this.precioClub=data.precioClub,
                    this.fotoTarjetaOfertaClub=data.fotoTarjetaOfertaClub,
                    this.fotoCaruselOfertaClub=data.fotoCaruselOfertaClub,
                    this.fotoDestacado=data.fotoDestacado

                })
                .catch(err => {
                    console.error(err);
                    this.error=true;
                    console.log("Error en el fetchData de la base de datos en producto_editar.js");                  
                })
        },
        modificar() {
            let producto = {
                nombre:this.nombre,
                descripcion:this.descripcion,
                fotoTarjeta:this,fotoTarjeta,
                precio:this.precio,
                stock:this.stock,
                precioClub:this.precioClub,
                fotoTarjetaOfertaClub:this.fotoTarjetaOfertaClub,
                fotoCaruselOfertaClub:this.fotoCaruselOfertaClub,
                fotoDestacado:this.fotoDestacado
            }
            var options = {
                body: JSON.stringify(producto),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
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