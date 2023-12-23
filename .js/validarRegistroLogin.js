document.addEventListener("DOMContentLoaded", function () {
    // Validar Login
    let mensajeL = document.getElementById("mensajeL");
    let emailLogin = document.getElementById("emailLogin");
    let passLogin = document.getElementById("passwordLogin");
    let formLogin = document.getElementById("formularioLogin");
  
    // Validar Registro
    let mensajeR = document.getElementById("mensajeR");
    let nombre = document.getElementById("nombreRegistro");
    let emailRegistro = document.getElementById("emailRegistro");
    let passRegistro = document.getElementById("passwordRegistro");
    let passRegistro2 = document.getElementById("passwordRegistro2");
    let formRegistro = document.getElementById("formularioRegistro");
  
    // Expresiones regulares
    let expRegEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let expRegText = /[A-Za-z]/;
  
    formLogin.addEventListener("submit", function (e) {
        e.preventDefault();
        let msj = "";
        let entrar = false;
        mensajeL.innerHTML = "";
  
        if (emailLogin.value.length === 0 || !expRegEmail.test(emailLogin.value)) {
            msj += "Ingrese un email válido<br>";
            entrar = true;
        }
  
        if (passLogin.value.length === 0) {
            msj += "Ingrese una contraseña<br>";
            entrar = true;
        }
  
        if (entrar) {
            mensajeL.innerHTML = msj;
        }
    });
  
    formRegistro.addEventListener("submit", function (e) {
        e.preventDefault();
        let msj = "";
        let entrar = false;
        mensajeR.innerHTML = "";
  
        if (!expRegText.test(nombre.value)) {
            msj += "El nombre no es válido<br>";
        }
  
        if (emailRegistro.value.length === 0 || !expRegEmail.test(emailRegistro.value)) {
            msj += "Ingrese un email válido<br>";
        }
  
        if (passRegistro.value.length === 0) {
            msj += "Ingrese una contraseña<br>";
            entrar = true;
        }
  
        if (passRegistro2.value !== passRegistro.value) {
            msj += "Las contraseñas son diferentes<br>";
            entrar = true;
        }
  
        if (entrar) {
            mensajeR.innerHTML = msj;
        }
    });
  });
  