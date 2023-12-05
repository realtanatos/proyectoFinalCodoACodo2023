//Login
//validar 
let mensajeL=document.getElementById("mensajeL");
let mensajeR=document.getElementById("mensajeR");
//login
let emailLogin=document.getElementById("emailLogin");
let passLogin=document.getElementById("passwordLogin");
let formLogin=document.getElementById("formularioLogin");
//register
let nombre=document.getElementById("nombreRegistro");
let emailRegistro=document.getElementById("emailRegistro");
let passRegistro=document.getElementById("passwordRegistro");
let passRegistro2=document.getElementById("passwordRegistro2");
let formRegistro=document.getElementById("formularioRegistro")
//expresiones regulares
let expRegEmail=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
let expRegtext=/[A-Za-z]/;
formLogin.addEventListener("submit",e=>{
    e.preventDefault()
    let msj="";
    let entrar=false;
    mensajeL.innerHTML=""
    if(emailLogin.value.length==0){
        msj+=`Ingrese un email<br>`
        entrar=true;
        
    }else if(!expRegEmail.test(emailLogin.value)){
        msj+=`El email no es valido <br>`
        entrar=true;
        
    }
    if(passLogin.value.length==0){
      msj+=`Ingrese una contraseña<br>`
      entrar=true;
    }
    if(entrar){
        mensajeL.innerHTML=msj
    }
    //al actualizar la pagina se pierden los cambios al menaje p
})

formRegistro.addEventListener("submit", e=>{
  e.preventDefault()
  let msj="";
    let entrar=false;
    mensajeR.innerHTML=""
    if(!expRegtext.test(nombre.value)){
      msj+=`El nombre no es valido<br>`
    }
    if(emailRegistro.value.length==0){
        msj+=`Ingrese un email<br>`
    }else if(!expRegEmail.test(emailRegistro.value)){
        msj+=`El email no es valido <br>`
        entrar=true;
    }
    if(passRegistro.value.length==0){
      msj+=`Ingrese una contraseña<br>`
      entrar=true;
    }
    if(passRegistro2.value!= passRegistro.value){
      msj+=`Las contraseñas son diferentes<br>`
      entrar=true;
    }
    if(entrar){
        // alert(msj)
        mensajeR.innerHTML=msj
    }
})

