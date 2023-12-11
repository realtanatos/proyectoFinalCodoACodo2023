const { createApp } = Vue
  createApp({
    data() {
      return {
        productos:[],
 //      url:'http://localhost:5000/productos', 
   // si el backend esta corriendo local  usar localhost 5000(si no lo subieron a pythonanywhere)
        url:'https://thanathosar.pythonanywhere.com/productos',   // si ya lo subieron a pythonanywhere
        error:false,
        cargando:true,
        /*atributos para el guardar los valores del formulario */
        nombre:"",
        descripcion:"",
        fotoTarjeta:"",
        precio:0,
        stock:0,
        precioClub:0,
        fotoTarjetaOfertaClub:"",
        fotoCaruselOfertaClub:"",
        fotoDestacado:"",

    }  
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.productos = data;
                    this.cargando=false;
                    console.log("Ya termino de cargar el JSON");    
                })
                .catch(err => {
                    console.error(err);
                    this.error=true;
                    console.log("Error en el fetchData de la base de datos en productos.js");              
                })
        },
        eliminar(id) {
            const url = this.url+'/' + id;
            var options = {
                method: 'DELETE',
            }
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
			 alert('Registro Eliminado')
                    location.reload(); // recarga el json luego de eliminado el registro
                })
        },

        grabar(){
            let producto = {
                nombreProducto:this.nombre,
                descripcionProducto:this.descripcion,
                fotoTarjetaProducto:this.fotoTarjeta,
                precioProducto:this.precio,
                stockProducto:this.stock,
                precioClubProducto:this.precioClub,
                fotoTarjetaOfertaClubProducto:this.fotoTarjetaOfertaClub,
                fotoCaruselOfertaClubProducto:this.fotoCaruselOfertaClub,
                fotoDestacadoProducto:this.fotoDestacado
            }
            console.log(producto);     
            var options = {
                body:JSON.stringify(producto),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            console.log(this.url); 
            fetch(this.url, options)
                .then(function () {
                    alert("Registro grabado")
                    window.location.href = "./productos.html";  // recarga productos.html
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar")  // puedo mostrar el error tambien
                })      
        }
    },
    created() {
        this.fetchData(this.url)
        console.log("CREADO Y!");    
    },
  }).mount('#app')