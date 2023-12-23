document.addEventListener('DOMContentLoaded', function () {
    // Verificar si los elementos existen
    console.log(document.getElementById("bRegistrar"));
    console.log(document.getElementById("bIniciarSession"));
    // css del registro y login
    document.getElementById("bRegistrar").addEventListener("click", registro);
    document.getElementById("bIniciarSession").addEventListener("click", login);
    // window.addEventListener("resize",anchoPag);

    let cajaAtras = document.querySelector(".cajaAtras");
    let cajaAtrasDiv = document.querySelector(".cajaAtras div");
    let contenedorLoginRegistro = document.querySelector(".contenedorLoginRegistro");
    let formularioLogin = document.querySelector(".formularioLogin");
    let formularioRegistro = document.querySelector(".formularioRegistro");
    let cajaAtrasLogin = document.querySelector(".cajaLogin");
    let cajaAtrasRegistro = document.querySelector(".cajaRegistro");

    // function anchoPag(){

    //     if(window.innerWidth>768){

    //     }else{

    //     }

    // }
    // anchoPag();

    function registro() {
        formularioRegistro.style.display = "block";
        formularioLogin.style.display = "none";
        cajaAtras.style.height = "820px";
        cajaAtrasRegistro.style.display = "none";
        cajaAtrasRegistro.style.opacity = "0";
        cajaAtrasLogin.style.display = "block";
        cajaAtrasLogin.style.opacity = "1";
    }

    function login() {
        formularioRegistro.style.display = "none";
        formularioLogin.style.display = "block";
        cajaAtras.style.height = "720px";
        cajaAtrasRegistro.style.display = "block";
        cajaAtrasRegistro.style.opacity = "1";
        cajaAtrasLogin.style.display = "none";
        cajaAtrasLogin.style.opacity = "0";
    }

    //fin del css
    //consumo de json para oferta en registro

    fetch('vinosLocal.json')
        .then(response => response.json())
        .then(data => {
            const ofertasSidebar = document.getElementById('ofertas-sidebar');
            let num = parseInt((Math.random() * 21) + 1)

            data.forEach(oferta => {
                if (oferta.id == num) {
                    const ofertaCard = document.createElement('div');
                    ofertaCard.classList.add('oferta-card');
                    ofertaCard.innerHTML = `
                    <h2 class="nombreOferta">${oferta.nombre}</h2>
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
            let num2 = parseInt((Math.random() * 21) + 1)

            data.forEach(oferta => {
                if (oferta.id == num2) {
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
});
