document.addEventListener('DOMContentLoaded', function () {
        // Vue app for managing cart data
        const app = Vue.createApp({
            data() {
                return {
                    cartItemCount: 0,
                };
            },
        });
    
        // Add the cart icon to the menu
        let menuContent = `
            <img src="./imagenes/isologotipo-saraza-wine-club-redux.png" alt="Logo Saraza Wine Club" class="isotipo">
            <br>
            <menunav>
                <a class="navheader" href="index.html">Inicio</a>
                <a class="navheader" href="tienda-fabian.html">Tienda</a>
                <a class="navheader" href="carrito-fabian.html">Carrito</a>
                <a class="navheader" href="registerLogin-fabian.html">Login</a>
                <a class="navheader" href="quienesSomos-fabian.html">¿Quiénes somos?</a>
                <a class="navheader" id="admi" href="productos.html">Administrar</a>
            </menunav>`;
    
        // Cart icon
        menuContent += `
            <div id="cart-icon-container">
                <a href="carrito-fabian.html">
                    <div id="cart-icon">
                        <img src="./imagenes/pngimg.com - shopping_cart_PNG20.png" alt="Shopping Cart">
                        <span id="cart-item-count">{{ cartItemCount }}</span>
                    </div>
                </a>
            </div>`;
    
        document.querySelector("header").innerHTML = menuContent;
    
        // Additional code for the footer
        let footerContent = `
            <b>© 2023 Sitio Desarrollado para Codo a Codo por Eduardo Argento - Franco Kerlin - Ximena Melendez - Ivan Reartes</b>`;
        
        document.querySelector("footer").innerHTML = footerContent;
    
        // Display the "Administrar" link based on the user
        if (sessionStorage.getItem('usuario') === "Franco") {
            let administrar = document.querySelector("#admi");
            administrar.style.display = "block";
        }
    
        // Create a Vue component for the cart
        app.component('cart', {
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
    
        // Mount the Vue app
        const vm = app.mount('#app');
    
        // Your existing code for the cart functionality (e.g., updating cart count) can be added here
    
        // Example: update the cart count
        // vm.cartItemCount = updatedItemCount;
    });
    