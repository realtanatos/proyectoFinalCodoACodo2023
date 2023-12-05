function crearTarjetasProductosCarrito() {
    fetch('carrito.json')
        .then(response => response.json())
        .then(data => {
            



        })



}







// const contenedorTarjetas = document.getElementById("cart-container");
// const cantidadElement = document.getElementById("cantidad");
// const precioElement = document.getElementById("precio");
// const carritoVacioElement = document.getElementById("carrito-vacio");
// const totalesContainer = document.getElementById("totales");

/** Crea las tarjetas de productos teniendo en cuenta lo guardado en localstorage */
// function crearTarjetasProductosCarrito() {
//     contenedorTarjetas.innerHTML = "";
//     fetch('vinosLocal.json')
//         .then(response => response.json())
//         .then(data => {
//             const productos = document.getElementById('contenidoTienda');
//                 console.log("Esto")
//                 data.forEach(producto => {
//                     const nuevoVino = document.createElement("div");
//                     nuevoVino.classList = "tarjeta-producto";
//                     nuevoVino.innerHTML = `
//     <img src="${producto.fotoTarjeta}" alt="Vinos">
//     <h3>${producto.nombre}</h3>
//     <span>$${producto.precio}</span>
//     <div>
//     <button>-</button>
//     <span class="cantidad">${producto.stock}</span>
//     <button>+</button>
//     </div>
//     `;
//                     contenedorTarjetas.appendChild(nuevoVino);
//                     nuevoVino
//                         .getElementsByTagName("button")[0]
//                         .addEventListener("click", (e) => {
//                             const cantidadElement = e.target.parentElement.getElementsByClassName("cantidad")[0];
//                             cantidadElement.innerText = restarAlCarrito(producto);
//                             crearTarjetasProductosCarrito();
//                             actualizarTotales();
//                         });
//                     nuevoVino
//                         .getElementsByTagName("button")[1]
//                         .addEventListener("click", (e) => {
//                             const cantidadElement = e.target.parentElement.getElementsByClassName("cantidad")[0];
//                             cantidadElement.innerText = agregarAlCarrito(producto);
//                             actualizarTotales();
//                         });



//                 });
            
//             revisarMensajeVacio();
//             actualizarTotales();
//             actualizarNumeroCarrito();
//         });



    
// }

// crearTarjetasProductosCarrito();

/** Actualiza el total de precio y unidades de la página del carrito */
// function actualizarTotales() {
//     fetch('vinosLocal.json')
//         .then(response => response.json())
//         .then(data => {
//             const productos = document.getElementById('contenidoCarrito');
//             let cantidad = 0;
//             let precio = 0;
//             // if (productos && productos.length > 0) {
//                 data.forEach(producto => {
//                     cantidad += producto.stock;
//                     precio += producto.precio * producto.cantidad;
//                 });
//             // }
//             cantidadElement.innerText = cantidad;
//             precioElement.innerText = precio;
//             if (precio === 0) {
//                 reiniciarCarrito();
//                 revisarMensajeVacio();
//             }

//         });



   
// }

// document.getElementById("reiniciar").addEventListener("click", () => {
//     contenedorTarjetas.innerHTML = "";
//     reiniciarCarrito();
//     revisarMensajeVacio();
// });



/** Muestra o esconde el mensaje de que no hay nada en el carrito */
// function revisarMensajeVacio() {
//     fetch('vinosLocal.json')
//         .then(response => response.json())
//         .then(data => {
//             const productos = document.getElementById('contenidoCarrito');
//             carritoVacioElement.classList.toggle("escondido", productos);
//             totalesContainer.classList.toggle("escondido", !productos);

//         });

// }