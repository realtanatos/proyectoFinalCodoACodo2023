fetch('vinosLocal.json')
  .then(response => response.json())
  .then(data => {
    const contenidoTienda = document.getElementById('contenidoTienda');
    
    // Recorre los productos y crea tarjetas para mostrarlos en la página.
    data.forEach(producto => {
      const productoCard = document.createElement('div');
      productoCard.classList.add('productoCard');
      productoCard.innerHTML = `
        <h3>${producto.nombre}</h3>
        <img src="${producto.fotoTarjeta}" alt="${producto.nombre}" class="card">
        <p>${producto.descripcion}</p>
        <p>Precio: $${producto.precio}</p>
        <button class="agregarAlCarrito" data-producto='${JSON.stringify(producto)}'>Agregar al Carrito</button>
      `;
      contenidoTienda.appendChild(productoCard);
    });

    // Agregar un manejador de eventos para el botón "Agregar al Carrito".
    const botonesAgregarCarrito = document.querySelectorAll('.agregarAlCarrito');
    botonesAgregarCarrito.forEach(boton => {
      boton.addEventListener('click', agregarAlCarrito);
    });

    function agregarAlCarrito() {
      const producto = JSON.parse(this.getAttribute('data-producto'));
      // Aquí puedes agregar la lógica para agregar el producto al carrito.
      console.log('Producto agregado al carrito:', producto);
    }
  })
  .catch(error => {
    console.error('Error al cargar los productos: ', error);
  });






// fetch('vinosLocal.json')
//     .then(response => response.json())
//     .then(data => {
//         const ofertasSidebar = document.getElementById('contenidoTienda');
//         const contenedorTarjetas = document.getElementById("contenidoTienda");
//         data.forEach(oferta => {
//             let num = 0;
//             const ofertaCard = document.createElement('div');
//             ofertaCard.classList.add('productoCard');
//             if (num <= 5) {
//                 ofertaCard.innerHTML = `
//                     <h3>${oferta.nombre}</h3>
//                     <span class="">
//                     <img src="${oferta.fotoTarjeta}" alt=""
//                     class="card" >
//                     </span>
//                     <div class="">
//                     <span class="descripTienda">
//                     <p>${oferta.descripcion}</p>
//                     <button id="restarCantidad">-</button>
//                     <p id="cantidadProducto">0</p>
//                     <button id="sumarCantidad">+</button>
//                     <br>
//                     <button id="botonCompra">Comprar</button>
                    
//                     </span>
//                     <div class="preciosTienda">
//                     <h2>${oferta.precio}</h2>
//                     <span class=precioClub>
//                     <h2>${oferta.precioClub}</h2>
//                     </span>
                    
//                     </div>
                    
//                     </div>
//                 `;
//                 num++;
//             }


//             ofertasSidebar.appendChild(ofertaCard);
//             document.getElementById("botonCompra").addEventListener("click", comprar);
//             // document.getElementById("sumarCantidad").addEventListener("click", sumar);
//             // document.getElementById("restarCantidad").addEventListener("click", restar);
 

//             function comprar() {
//                 // Obtener el producto que el usuario desea comprar
//                 const producto = data.find((oferta) => oferta.nombre === this.closest(".productoCard").querySelector("h3").textContent);
              
//                 // Obtener el carrito de compras
//                 const carrito = JSON.parse(document.querySelector("carrito.json").textContent)[0];
              
//                 // Agregar el producto al carrito de compras
//                 if (this.parentNode && carrito) {
//                   carrito.productos.push({
//                     nombre: producto.nombre,
//                     precio: producto.precio,
//                     cantidad: 1
//                   });
              
//                   // Guardar el carrito en el archivo JSON
//                   const json = JSON.stringify(carrito);
//                   document.querySelector("#carrito").textContent = json;
//                   console.log(json)
                  
//                 }
                
//               }
              






//         });


//     })
//     .catch(error => {
//         console.error('Error al cargar las ofertas: ', error);
//     });



