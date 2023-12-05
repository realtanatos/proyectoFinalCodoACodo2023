let cad = `
<img src="./imagenes/isologotipo-saraza-wine-club-redux.png" alt="Logo Saraza Wine Club" class="isotipo">
<br>
        <menunav>
            
            <a class="navheader" href="index.html">Inicio</a>
            <a class="navheader" href="tienda-fabian.html">Tienda</a>
            <a class="navheader" href="carrito-fabian.html">Carrito</a>
            <a class="navheader" href="registerLogin-fabian.html">Login</a>
            <a class="navheader" href="quienesSomos-fabian.html">Quienes Somos</a>
        </menunav> `

document.querySelector("header").innerHTML = cad
//<b class="logotipo">Saraza Wine Club</b> se quito temporalmente para ver como queda 

cad = `
        <b>© 2023 Sitio Desarrollado para Codo a Codo por Eduardo Argento - Franco Kerlin - Ximena Melendez - Ivan Reartes</b>
        `



document.querySelector("footer").innerHTML = cad


      