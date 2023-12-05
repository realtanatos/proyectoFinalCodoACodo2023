


    var app = new Vue({
        el: '#app',
        data: {
            registros: []
        },
        created: function () {
            // Continuar con cualquier procesamiento que necesites
        }
    });

    function cargarArchivo() {
        var input = document.getElementById('jsonInput');
        var file = input.files[0];

        if (file) {
            var reader = new FileReader();
            reader.onload = function(e) {
                var contenido = e.target.result;
                var data = JSON.parse(contenido);
                console.log("JSON cargado correctamente.");
                console.log(data);

                // Almacenar los datos en localStorage
                localStorage.setItem('wineRecords', JSON.stringify(data));

                // Continuar con cualquier procesamiento adicional que necesites
            };
            reader.readAsText(file);
        }
    };

// usando los datos almacenados en localstorage de todos estos registros, seleccione a dos al azar
// del primero mmostrar una tarjeta html con class id=destacado con la imagen, el nombre, descripcion
// y un link a su pagina correspondiente dentro de mi tienda
// del segundo mostrar una tarjeta html con class id=ofertaClub con la imagen, el nombre
// el precio de descuento del club para socios, y un link para dirigirme a la pagina de ese
// vino dentro de la tienda.



// Paso 1: Recuperar los registros almacenados en el localStorage
var registros = JSON.parse(localStorage.getItem('wineRecords'));

// Paso 2: Seleccionar dos registros al azar
var keys = Object.keys(registros);
var indice1 = Math.floor(Math.random() * keys.length);
var indice2 = Math.floor(Math.random() * keys.length);

// Paso 3: Obtener los datos de los registros seleccionados
var registro1 = registros[keys[indice1]];
var registro2 = registros[keys[indice2]];

// Paso 4: Generar las tarjetas HTML

// Tarjeta HTML para el primer registro (ID=destacado)
var tarjetaDestacada = document.createElement('div');
tarjetaDestacada.classList.add('tarjeta', 'destacado');
tarjetaDestacada.innerHTML = `
    <img src="${registro1['fotoDestacado']}" alt="${registro1.nombre}">
    <h2>${registro1.nombre}</h2>
    <p>${registro1.descripcion}</p>
    <a href="${registro1.link}" class="enlace-tienda">Ver más</a>
`;

// Tarjeta HTML para el segundo registro (ID=ofertaClub)
var tarjetaOfertaClub = document.createElement('div');
tarjetaOfertaClub.classList.add('tarjeta', 'ofertaClub');
tarjetaOfertaClub.innerHTML = `
    <img src="${registro2['fotoTarjetaOfertaClub']}" alt="${registro2.nombre}">
    <h2>${registro2.nombre}</h2>
    <p>Precio de descuento para socios: $${registro2['precioClub']}</p>
    <a href="${registro2.link}" class="enlace-tienda">Ver más</a>
`;

// Paso 5: Agregar las tarjetas al documento HTML
document.getElementById('contenedor').appendChild(tarjetaDestacada);
document.getElementById('contenedor').appendChild(tarjetaOfertaClub);
