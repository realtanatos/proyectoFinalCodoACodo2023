document.addEventListener("DOMContentLoaded", function () {
    new Vue({
      el: "#randomHeroImage",
      data: {
        imagenes: [
            "../imagenes/heroImage1.png",
            "../imagenes/heroImage2.png",
            "../imagenes/heroImage3.png",
            "../imagenes/heroImage4.png"
        ],
        imagenSeleccionada: ""
      }
    });
  });
  