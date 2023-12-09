console.log(location.search); // lee los argumentos pasados a este formulario
var id = location.search.substr(4); // producto_update.html?id=1
console.log(id);
const { createApp } = Vue;

createApp({
    data() {
        return {
            id: 0,
            nombreUsuario: "",
            nombreApellido: "",
            email: "",
            clave: "",
            telefonoFijo: "",
            telefonoCelular: "",
            miembroClub: false,
            direccionCliente: "",
            pisoDeptoCliente: "",
            codigoPostalCliente: "",
            localidadCliente: "",
            provinciaCliente: "",
            url: 'https://thanathosar.pythonanywhere.com/clientes/' + id,
        };
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log("Datos obtenidos:", data);
                    this.id = data.id;
                    this.nombreUsuario = data.nombreUsuario;
                    this.nombreApellido = data.nombreApellido;
                    this.email = data.email;
                    this.clave = data.clave;
                    this.telefonoFijo = data.telefonoFijo;
                    this.telefonoCelular = data.telefonoCelular;
                    if (data.miembroClub==1){
                        this.miembroClub=true;
                    }else{
                        this.miembroClub=false;
                    }
                    console.log(this.clave)
                    this.direccionCliente = data.direccionCliente;
                    this.pisoDeptoCliente = data.pisoDeptoCliente;
                    this.codigoPostalCliente = data.codigoPostalCliente;
                    this.localidadCliente = data.localidadCliente;
                    this.provinciaCliente = data.provinciaCliente;
                    
                })
                .catch(err => {
                    console.error(err);
                    this.error = true;
                    console.log("Error en el fetchData de la base de datos en clientesCRUD_editar.js");
                });
        },
        modificar() {
            console.log("1")
            let cliente = {
                id: this.id,
                nombreUsuario: this.nombreUsuario,
                nombreApellido: this.nombreApellido,
                email: this.email,
                clave: this.clave,
                telefonoFijo: this.telefonoFijo,
                telefonoCelular: this.telefonoCelular,
                miembroClub: this.miembroClub,
                direccionCliente: this.direccionCliente,
                pisoDeptoCliente: this.pisoDeptoCliente,
                codigoPostalCliente: this.codigoPostalCliente,
                localidadCliente: this.localidadCliente,
                provinciaCliente: this.provinciaCliente
            };

            console.log("Datos a enviar:", cliente);

            var options = {
                body: JSON.stringify(cliente),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            };

            fetch(this.url, options)
                .then(() => {
                    console.log("Registro modificado con éxito");
                    alert("Registro modificado");
                    window.location.href = "./clientesCRUD.html";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar");
                });
        }
    },
    created() {
        console.log(this.url)
        this.fetchData(this.url);
    },
}).mount('#formularioRegistro');
