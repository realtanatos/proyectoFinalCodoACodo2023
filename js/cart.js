const contenedorTarjetas = document.getElementById("cart-container");
const cantidadElement = document.getElementById("cantidad");
const precioElement = document.getElementById("precio");
const carritoVacioElement = document.getElementById("carrito-vacio");
const totalesContainer = document.getElementById("totales");

/** Crea las tarjetas de productos teniendo en cuenta lo guardado en localstorage */
function crearTarjetasProductosCarrito() {
  contenedorTarjetas.innerHTML = "";
  const productos = JSON.parse(localStorage.getItem("vinos"));
  if (productos && productos.length > 0) {
    productos.forEach((producto) => {
      const nuevoVino = document.createElement("div");
      nuevoVino.classList = "tarjeta-producto";
      nuevoVino.innerHTML = `
    <img src="imagenes/bodega/vino${producto.id}.jpg" alt="Vinos" class="card">
    <h3>${producto.nombre}</h3>
    <span class="descripTienda">
    <p>${producto.descripcion}</p>
    </span>
    <span>$${producto.precio}</span>
    <div>
    <button>-</button>
    <span class="cantidad">${producto.cantidad}</span>
    <button>+</button>
    </div>
    `;
      contenedorTarjetas.appendChild(nuevoVino);
      nuevoVino
        .getElementsByTagName("button")[0]
        .addEventListener("click", (e) => {
          const cantidadElement = e.target.parentElement.getElementsByClassName("cantidad")[0];
          cantidadElement.innerText = restarAlCarrito(producto);
          crearTarjetasProductosCarrito();
          actualizarTotales();
        });
      nuevoVino
        .getElementsByTagName("button")[1]
        .addEventListener("click", (e) => {
          const cantidadElement = e.target.parentElement.getElementsByClassName("cantidad")[0];
          cantidadElement.innerText = agregarAlCarrito(producto);
          actualizarTotales();
        });
    });
  }
  revisarMensajeVacio();
  actualizarTotales();
  // actualizarNumeroCarrito();
}

crearTarjetasProductosCarrito();

/** Actualiza el total de precio y unidades de la página del carrito */
function actualizarTotales() {
  const productos = JSON.parse(localStorage.getItem("vinos"));
  let cantidad = 0;
  let precio = 0;
  if (productos && productos.length > 0) {
    productos.forEach((producto) => {
      cantidad += producto.cantidad;
      precio += producto.precio * producto.cantidad;
    });
  }
  cantidadElement.innerText = cantidad;
  precioElement.innerText = precio;
  if(precio === 0) {
    reiniciarCarrito();
    revisarMensajeVacio();
  }
}

document.getElementById("reiniciar").addEventListener("click", () => {
  contenedorTarjetas.innerHTML = "";
  reiniciarCarrito();
  revisarMensajeVacio();
});



/** Muestra o esconde el mensaje de que no hay nada en el carrito */
function revisarMensajeVacio() {
  const productos = JSON.parse(localStorage.getItem("vinos"));
  carritoVacioElement.classList.toggle("escondido", productos);
  totalesContainer.classList.toggle("escondido", !productos);
}


function crearOfertas(){
  fetch('vinosLocal.json') 
        .then(response => response.json())
        .then(data => {
            const ofertasSidebar = document.getElementById('ofertas-sidebar');
            let num=parseInt((Math.random()*21)+1)
            
            data.forEach(oferta => {
                if(oferta.id==num){
                    const ofertaCard = document.createElement('div');
                ofertaCard.classList.add('oferta-card');
                ofertaCard.innerHTML = `
                    <h3>${oferta.nombre}</h3>
                    <span class="imgOfertaClub">
                    <img src="${oferta.fotoTarjeta}" alt="imgOfertaClub"
                    class="widget" >
                    </span>
                    <div class="precioDes">
                    <span class="descrip">
                    <p>${oferta.descripcion}</p>
                    </span>
                    <div class="precios">
                    <p><del>${oferta.precio}</del></p>
                    <span class=precioClub>
                    <h2>${oferta.precioClub}</h2>
                    </span>
                    
                    </div>
                    
                    </div>
                `;
                //<a href="${oferta.enlace}" target="blank">Ver oferta</a>
                ofertasSidebar.appendChild(ofertaCard);
                }
                
            });
            const ofertasSidebar2 = document.getElementById('ofertas-sidebar2');
            let num2=parseInt((Math.random()*21)+1)
            
            data.forEach(oferta => {
                if(oferta.id==num2){
                    const ofertaCard2 = document.createElement('div');
                ofertaCard2.classList.add('oferta-card2');
                ofertaCard2.innerHTML = `                    
                    <h3>${oferta.nombre}</h3>
                    <span class="imgOfertaClub">
                    <img src="${oferta.fotoTarjeta}" alt="imgOfertaClub"
                    class="widget" >
                    </span>
                    <div class="precioDes">
                    <span class="descrip">
                    <p>${oferta.descripcion}</p>
                    </span>
                    <div class="precios">
                    <p><del>${oferta.precio}</del></p>
                    <span class=precioClub>
                    <h2>${oferta.precioClub}</h2>
                    </span>
                    
                    </div>
                    
                    </div>
                `;
                //<a href="${oferta.enlace}" target="blank">Ver oferta</a>
                ofertasSidebar2.appendChild(ofertaCard2);
                }
                
            });

        })
        .catch(error => {
            console.error('Error al cargar las ofertas: ', error);
        });
}
crearOfertas();