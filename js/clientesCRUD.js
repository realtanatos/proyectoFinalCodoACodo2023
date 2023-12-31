// clientes.js

const { createApp } = Vue;

createApp({
    data() {
        return {
            clientes: [],
            nombreUsuario: "",
            nombreApellido: "",
            email: "",
            clave : "",
            telefonoFijo : "",
            telefonoCelular : "",
            miembroClub : false,
            direccionCliente : "",
            pisoDeptoCliente : "",
            codigoPostalCliente : "",
            localidadCliente : "",
            provinciaCliente : ""
                };
    },
    methods: {
        fetchData() {
            fetch('https://thanathosar.pythonanywhere.com/clientes')
                .then(response => response.json())
                .then(data => {
                    this.clientes = data;
                })
                .catch(error => {
                    console.error('Error al obtener clientes:', error);
                });
        },
        agregarCliente() {
            console.log("Formulario enviado");
            const nuevoCliente = {
                nombreUsuario: this.nombreUsuario,
                nombreApellido: this.nombreApellido,
                email: this.email,
                clave: this.clave,
                telefonoFijo: this.telefonoFijo,
                telefonoCelular: this.telefonoCelular,
                miembroClub: Boolean(this.miembroClub), // Convertir a booleano
                direccionCliente: this.direccionCliente,
                pisoDeptoCliente: this.pisoDeptoCliente,
                codigoPostalCliente: this.codigoPostalCliente,
                localidadCliente: this.localidadCliente,
                provinciaCliente: this.provinciaCliente
            };
            
            console.log('Nuevo cliente a agregar:', nuevoCliente);

            fetch('https://thanathosar.pythonanywhere.com/clientes', {
                body: JSON.stringify(nuevoCliente),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
                
            })
            .then(response => response.json())
            .then(data => {
                console.log('Cliente creado:', data);
                window.location.reload();
                this.fetchData(); // Actualizar la lista después de agregar
            })
            .catch(error => {
                console.error('Error al agregar cliente:', error);
            });
        
        },
        eliminarCliente(id) {
           
            const url = `https://thanathosar.pythonanywhere.com/clientes/${id}`;
            var options = {
                method: 'DELETE',
                
            };
            console.log("entra ")
            fetch(url, options)
                .then(res => res.json())
                .then(res => {
                    alert('Cliente Eliminado');
                    this.fetchData(); // Actualizar la lista después de eliminar
                })
                .catch(error => {
                    console.error('Error al eliminar cliente:', error);
                });
        },
        // Otros métodos para editar y actualizar clientes
    },
    created() {
        this.fetchData();
    },
}).mount('#formularioRegistro');
