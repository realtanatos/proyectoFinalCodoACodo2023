document.addEventListener("DOMContentLoaded", function () {
    const API_URL = "https://thanathosar.pythonanywhere.com/clientes";
    const emailLogin = document.getElementById("emailLogin");
    const passLogin = document.getElementById("passwordLogin");

    document.getElementById("formularioLogin").addEventListener("submit", function (event) {
        event.preventDefault(); // Evita que el formulario se envíe

        // Obten los valores actuales de los campos de entrada
        const emailValue = emailLogin.value;
        const passValue = passLogin.value;

        console.log("Valores de email y contraseña:", emailValue, passValue);

        fetch(API_URL)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.text();
            })
            .then((data) => {
                console.log("Respuesta del servidor:", data);
                try {
                    const users = JSON.parse(data);
                    let userFound = false;

                    users.forEach((element) => {
                        if (emailValue === element.email && passValue === element.clave) {
                            userFound = true;
                        }
                    });

                    if (userFound) {
                        console.log("Usuario encontrado. Iniciando sesión correctamente.");
                        alert("Has iniciado sesión correctamente");
                    } else {
                        console.log("Usuario o contraseña incorrectos.");
                        alert("Usuario o contraseña incorrectos");
                    }
                } catch (parseError) {
                    console.error("Error al analizar JSON:", parseError);
                    alert("Hubo un error al intentar iniciar sesión. Por favor, inténtalo de nuevo.");
                }
            })
            .catch((error) => {
                console.error("Error al obtener usuarios:", error);
                alert("Hubo un error al intentar iniciar sesión. Por favor, inténtalo de nuevo.");
            });
    });
});
