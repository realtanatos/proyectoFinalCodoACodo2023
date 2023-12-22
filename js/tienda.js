document.addEventListener('DOMContentLoaded', function () {
    // Aplicación Vue para gestionar los datos del carrito
    const appTienda = Vue.createApp({
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
            realizarBusqueda() {
                alert("EL BUSCADOR Y LA TIENDA SE IMPLEMENTARÁN PRONTO");
                // Puedes realizar otras acciones relacionadas con la búsqueda aquí
            },
        },
    });

    // Componente Vue para el carrito
    appTienda.component('cart', {
        props: ['cartItemCount'], // Asegúrate de definir las props correctamente
        template: `
            <div class="cart-icon-container">
                <a href="carrito-fabian.html">
                    <div class="cart-icon">
                        <img src="./imagenes/pngimg.com - shopping_cart_PNG20.png" alt="Shopping Cart">
                        <span class="cart-item-count">{{ cartItemCount }}</span>
                    </div>
                </a>
            </div>`,
    });

    // Monta la aplicación Vue en la div #tienda
    const vmTienda = appTienda.mount('#tienda');
});
