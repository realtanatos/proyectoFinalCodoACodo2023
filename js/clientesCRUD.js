const { createApp } = Vue;

createApp({
    data() {
        return {
            clientes: [],
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
            error: null, // Para manejar errores
        };
    },
    methods: {
        async fetchData() {
            try {
                const response = await fetch('https://thanathosar.pythonanywhere.com/clientes');
                if (!response.ok) {
                    throw new Error('Error al obtener clientes');
                }
                this.clientes = await response.json();
            } catch (error) {
                console.error('Error al obtener clientes:', error.message);
            }
        },
        async agregarCliente() {
            console.log("Formulario enviado");
            const nuevoCliente = {
                nombreUsuario: this.nombreUsuario,
                nombreApellido: this.nombreApellido,
                email: this.email,
                clave: this.clave,
                telefonoFijo: this.telefonoFijo,
                telefonoCelular: this.telefonoCelular,
                miembroClub: Boolean(this.miembroClub),
                direccionCliente: this.direccionCliente,
                pisoDeptoCliente: this.pisoDeptoCliente,
                codigoPostalCliente: this.codigoPostalCliente,
                localidadCliente: this.localidadCliente,
                provinciaCliente: this.provinciaCliente
            };

            try {
                const response = await fetch('https://thanathosar.pythonanywhere.com/clientes', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(nuevoCliente),
                });

                if (!response.ok) {
                    throw new Error('Error al agregar cliente');
                }

                const data = await response.json();
                console.log('Cliente creado:', data);
                alert("EL USUARIO YA SE HA AGREGADO");

                // Actualizar la lista después de agregar sin recargar la página
                this.fetchData();
            } catch (error) {
                console.error('Error al agregar cliente:', error.message);
                this.error = 'Error al agregar cliente';
            }
        },
        async eliminarCliente(id) {
            const url = `https://thanathosar.pythonanywhere.com/clientes/${id}`;
            
            try {
                const response = await fetch(url, { method: 'DELETE' });

                if (!response.ok) {
                    throw new Error('Error al eliminar cliente');
                }

                console.log('Cliente eliminado:', id);
                this.fetchData(); // Actualizar la lista después de eliminar
            } catch (error) {
                console.error('Error al eliminar cliente:', error.message);
                this.error = 'Error al eliminar cliente';
            }
        },
        // Otros métodos para editar y actualizar clientes
    },
    created() {
        this.fetchData();
    },
}).mount('#formularioRegistro');
