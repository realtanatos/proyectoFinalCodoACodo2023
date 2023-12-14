const cuentaCarritoElement = document.getElementById("cuenta-carrito");

// Función para obtener los datos del carrito desde localStorage
function getCartFromLocalStorage() {
  return JSON.parse(localStorage.getItem("vinos")) || [];
}

// Función para actualizar los datos del carrito en localStorage
function updateCartInLocalStorage(cart) {
  localStorage.setItem("vinos", JSON.stringify(cart));
}

function agregarAlCarrito(producto) {
  let memoria = getCartFromLocalStorage();
  let cantidadProductoFinal;

  const indiceProducto = memoria.findIndex(vinosLocal => vinosLocal.id === producto.id);

  if (indiceProducto === -1) {
    const nuevoProducto = getNuevoProductoParaMemoria(producto);
    memoria.push(nuevoProducto);
    cantidadProductoFinal = 1;
  } else {
    memoria[indiceProducto].cantidad++;
    cantidadProductoFinal = memoria[indiceProducto].cantidad;
  }

  updateCartInLocalStorage(memoria);
  return cantidadProductoFinal;
}


function restarAlCarrito(producto) {
  // Obtengo los datos actuales del carrito
  let memoria = getCartFromLocalStorage();
  let cantidadProductoFinal = 0;

  // Busco el índice del producto en el carrito
  const indiceProducto = memoria.findIndex(vinosLocal => vinosLocal.id === producto.id);

  if (indiceProducto !== -1) {
    // Si el producto está en el carrito, decremento la cantidad
    memoria[indiceProducto].cantidad--;
    cantidadProductoFinal = memoria[indiceProducto].cantidad;

    if (cantidadProductoFinal === 0) {
      // Si la cantidad se vuelve cero, elimino el artículo del carrito
      memoria.splice(indiceProducto, 1);
    }

    // Actualizo los datos del carrito en localStorage
    updateCartInLocalStorage(memoria);

    // No need to update the UI here, it will be handled by the Vue component
  }

  return cantidadProductoFinal;
}


function getNuevoProductoParaMemoria(producto) {
  // Creo un nuevo objeto producto con una cantidad inicial de 1
  const nuevoProducto = { ...producto, cantidad: 1 };
  return nuevoProducto;
}

function reiniciarCarrito() {
  // Elimino todos los datos del carrito en localStorage
  localStorage.removeItem("vinos");
  // Actualizo la interfaz de usuario del carrito
  actualizarCarritoUI();
}

function actualizarCarritoUI(producto, cantidad) {
  console.log("Updating UI with:", producto, cantidad);
  // Update the cart UI with the product and quantities
  const cartContainer = document.getElementById("cart-container");
  const nuevoItem = document.createElement("div");
  nuevoItem.innerHTML = `${producto.nombre} - Cantidad: ${cantidad}`;
  cartContainer.appendChild(nuevoItem);

  // Update the cart item count in the icon
  const cartItemCount = document.getElementById('cart-item-count');
  cartItemCount.innerText = cantidad;
  console.log("UI updated successfully");
}

