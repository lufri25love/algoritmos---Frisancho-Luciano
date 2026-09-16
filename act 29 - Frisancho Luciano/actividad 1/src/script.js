/*
Ejercicio 1: Guardar Preferencias de Usuario
1. La función debe permitir al usuario ingresar su nombre y seleccionar su color
de fondo preferido desde una lista de opciones.
2. Los datos ingresados deben almacenarse en LocalStorage.
3. Cada vez que la página se recargue, las preferencias deben recuperarse de
LocalStorage y aplicarse automáticamente.
*/
window.onload = function() {
    cargarPreferencias();
};

function guardarPreferencias() {
    let nombre = document.getElementById("nombre").value;
    let color = document.getElementById("colorFondo").value;

    if (nombre !== "" && color !== "") {
        localStorage.setItem("nombreUsuario", nombre);
        localStorage.setItem("colorPreferido", color);
        cargarPreferencias();
    } else {
        alert("Por favor, ingrese un nombre y seleccione un color.");
    }
}

function cargarPreferencias() {
    let nombreGuardado = localStorage.getItem("nombreUsuario");
    let colorGuardado = localStorage.getItem("colorPreferido");

    if (nombreGuardado && colorGuardado) {
        document.body.style.backgroundColor = colorGuardado;

        document.getElementById("nombre").value = nombreGuardado;

        document.getElementById("colorFondo").value = colorGuardado;
    }
}