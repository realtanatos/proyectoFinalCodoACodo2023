document.addEventListener('DOMContentLoaded', function () {
    // Agrega el icono del carrito al menú
    let menuContent = `
        <img src="./imagenes/isologotipo-saraza-wine-club-redux.png" alt="Logo Saraza Wine Club" class="isotipo">
        <br>
        <menunav>
            <a class="navheader" href="index.html">Inicio</a>
            <a class="navheader" href="tienda-fabian.html">Tienda</a>
            <a class="navheader" href="carrito-fabian.html" id="bCarrito">Carrito</a>
            <a class="navheader" href="registerLogin-fabian.html" id="bIniciarSession">Login</a>
            <a class="navheader" href="quienesSomos-fabian.html">¿Quiénes somos?</a>
            <a class="navheader" href="productosCRUD.html">Administrar</a>
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

    // Código adicional para el nuevo contenido del pie de página
    let socialContent = `
        <img src="./imagenes/isologotipo-saraza-social-redux.png" alt="Logo Saraza Wine Club" class="social">
        <br>
        <h3>Seguinos en nuestras redes!</h3>
        <div class="wrapper">
            <i class="fa fa-5x fa-facebook-square" href="https://www.facebook.com/">.</i>
            <i class="fa fa-5x fa-twitter-square" href="https://www.twitter.com/home">.</i>
            <i class="fa fa-5x fa-github-square" href="https://www.github.com/">.</i>
            <i class="fa fa-5x fa-snapchat-square" href="https://www.snapchat.com">.</i>
        </div>
        <br>
        <br>
        <b>© 2023 Sitio Desarrollado para Codo a Codo por Eduardo Argento - Franco Kerlin - Ivan Reartes</b>`;

    document.querySelector("footer").innerHTML = socialContent;

    // Evento de clic para el botón "Carrito"
    const carritoButton = document.getElementById('bCarrito');
    carritoButton.addEventListener('click', function () {
        alert('EL CARRITO SE IMPLEMENTARÁ PRONTO');
    });
});
