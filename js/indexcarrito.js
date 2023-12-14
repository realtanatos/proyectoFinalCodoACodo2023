const contenedorTarjetas = document.getElementById("productos-container");
const URL = 'https://thanathosar.pythonanywhere.com/productos';

function crearTarjetasProductosInicio(productos) {
    productos.forEach(producto => {
        const nuevoVino = document.createElement("div");
        nuevoVino.classList = "tarjeta-producto";
        nuevoVino.innerHTML = `
        <img src=${producto.fotoTarjetaProducto} alt="Vinos" class="card">
        <h3>${producto.nombreProducto}</h3>
        <span class="descripTienda">
            <p>${producto.descripcionProducto}</p>
            <p class="stock">${producto.stockProducto}</p>
            <button>Agregar al carrito</button>
        </span>
        <p class="precio">$${producto.precioClubProducto}</p><br>
        `

        contenedorTarjetas.appendChild(nuevoVino);

        // Add event listener to the "Agregar al carrito" button
        nuevoVino.getElementsByTagName("button")[0].addEventListener("click", () => agregarAlCarritoYActualizarUI(producto));
    });
}

fetch(URL)
  .then(response => response.json())
  .then(data => {
    crearTarjetasProductosInicio(data);
  });

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

function agregarAlCarritoYActualizarUI(producto) {
  const cantidad = agregarAlCarrito(producto); // La funcion está en cartservice.js
  actualizarCarritoUI(producto, cantidad);
}

function actualizarCarritoUI(producto, cantidad) {
  // Actualiza el carrito UI con producto y cantidades
  const cartContainer = document.getElementById("cart-container");
  cartContainer.innerHTML = ''; // Elimina los items existentes

  const cart = getCartFromLocalStorage();

  cart.items.forEach(item => {
    const nuevoItem = document.createElement("div");
    nuevoItem.innerHTML = `${item.nombre} - Cantidad: ${item.cantidad}`;
    cartContainer.appendChild(nuevoItem);
  });
}







crearOfertas();