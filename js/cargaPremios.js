        // Función para obtener un número aleatorio entre un rango
        function getRandomNumber(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }

        // Función para cargar un archivo JSON
        function loadJSON(callback) {
            const xhr = new XMLHttpRequest();
            xhr.overrideMimeType("application/json");
            xhr.open("GET", "premios.json", true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    callback(xhr.responseText);
                }
            };
            xhr.send(null);
        }

// Función para verificar si un elemento está en la vista del usuario
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

/* un detalle cosmetico */

// Activar la animación cuando se vea la tarjeta
function animateOnScroll() {
    const cards = document.querySelectorAll(".card");

    cards.forEach((card) => {
        if (isElementInViewport(card)) {
            card.classList.add("animate__animated", "animate__fadeIn"); // Agrega clases de animación
        }
    });
}

// Solo ejecuta la función al cargar la página y cuando se hace scroll asi el usuario ve la animacion cuando llega
document.addEventListener("DOMContentLoaded", animateOnScroll);
window.addEventListener("scroll", animateOnScroll);


        // Generar tarjetas
        function generateCards(data) {
            const cardContainer = document.getElementById("contenedor-tarjeta");
            const jsonData = JSON.parse(data);

            // Obtener 3 índices random
            const randomIndexes = [];
            while (randomIndexes.length < 3) {
                const randomIndex = getRandomNumber(0, jsonData.length - 1);
                if (!randomIndexes.includes(randomIndex)) {
                    randomIndexes.push(randomIndex);
                }
            }

            // Crear las tarjetas con los 3 registros
            randomIndexes.forEach((index) => {
                const premio = jsonData[index];
                const card = document.createElement("div");
                card.classList.add("tarjeta-premios");
                card.innerHTML = `
                    <img src="${premio.imagen_persona}" alt="${premio.nombre}">
                    <p>"${premio.valoracion}"</p>    
                    <h4>${premio.nombre}</h4>
                    <p>${premio.cargo_directivo}</p>
                    <p>${premio.asociacion}</p>
                    <img src="${premio.imagen_premio}" alt="${premio.nombre_premio}">
                    <p>Premio: ${premio.nombre_premio}</p>
                    `;
                cardContainer.appendChild(card);
            });
        }

        // Cargar el archivo JSON y generar tarjetas
        loadJSON(generateCards);
        