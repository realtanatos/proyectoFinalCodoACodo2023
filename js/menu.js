document.addEventListener('DOMContentLoaded', function () {
        // Aplicación Vue para gestionar los datos del carrito
        const app = Vue.createApp({
                data() {
                        return {
                                cartItemCount: 0,
                        };
                },

                methods: {
                        // Método para agregar un producto al carrito
                        agregarAlCarrito(producto) {
                                // Llama a la función desde cartservice.js
                                const cantidad = agregarAlCarrito(producto);
                                // Actualiza la cantidad en el carrito
                                this.cartItemCount = cantidad;
                        },
                        // Método para restar un producto del carrito
                        restarAlCarrito(producto) {
                                // Llama a la función desde cartservice.js
                                const cantidad = restarAlCarrito(producto);
                                // Actualiza la cantidad en el carrito
                                this.cartItemCount = cantidad;
                        },
                },
        });

        // Componente Vue para el carrito
        app.component('cart', {
                props: ['cartItemCount'], // Asegúrate de definir las props correctamente
                template: `
                  <div id="cart-icon-container">
                    <a href="carrito-fabian.html">
                      <div id="cart-icon">
                        <img src="./imagenes/pngimg.com - shopping_cart_PNG20.png" alt="Shopping Cart">
                        <span id="cart-item-count">{{ cartItemCount }}</span>
                      </div>
                    </a>
                  </div>`,
        });

        // Monta la aplicación Vue
        const vm = app.mount('#app');

        // Agrega el icono del carrito al menú
        let menuContent = `
      <img src="./imagenes/isologotipo-saraza-wine-club-redux.png" alt="Logo Saraza Wine Club" class="isotipo">
      <br>
      <menunav>
        <a class="navheader" href="index.html">Inicio</a>
        <a class="navheader" href="tienda-fabian.html">Tienda</a>
        <a class="navheader" href="carrito-fabian.html">Carrito</a>
        <a class="navheader" href="registerLogin-fabian.html" id="bIniciarSession">Login</a>
        <a class="navheader" href="quienesSomos-fabian.html">¿Quiénes somos?</a>
        <a class="navheader" href="productos.html">Administrar</a>
        <a class="navheader" href="register-fabian.html" id="bRegistrar">Registrarse</a>
      </menunav>`;

        // Icono del carrito
        menuContent += `<cart @agregarAlCarrito="agregarAlCarrito" @restarAlCarrito="restarAlCarrito"></cart>`;

        console.log("Insertando contenido del menú en el HTML");
        document.querySelector("header").innerHTML = menuContent;

        // Código adicional para el pie de página
        let footerContent = `
          <b>© 2023 Sitio Desarrollado para Codo a Codo por Eduardo Argento - Franco Kerlin - Ivan Reartes</b>`;

        document.querySelector("footer").innerHTML = footerContent;

        // Muestra el enlace "Administrar" según el usuario
        if (sessionStorage.getItem('usuario') === "Franco") {
                let administrar = document.querySelector("#admi");
                administrar.style.display = "block";
        }
});
