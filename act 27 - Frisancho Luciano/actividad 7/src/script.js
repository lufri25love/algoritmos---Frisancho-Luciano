/*
7. Confeccionar una página que muestre tres checkbox que permitan
seleccionar los deportes que practica el usuario (Fútbol, Básquet, Tenis).
Mostrar al presionar un botón los deportes que eligió.
*/

function mostrarDeportes() {
    let chkFutbol = document.getElementById("futbol");
    let chkBasquet = document.getElementById("basquet");
    let chkTenis = document.getElementById("tenis");
    let seleccionados = [];
    if (chkFutbol.checked) {
        seleccionados.push(chkFutbol.value);
    }
    if (chkBasquet.checked) {
        seleccionados.push(chkBasquet.value);
    }
    if (chkTenis.checked) {
        seleccionados.push(chkTenis.value);
    }

    let mensaje = document.getElementById("resultado");
    if (seleccionados.length > 0) {
        mensaje.textContent = "Deportes seleccionados: " + seleccionados.join(", ");
    } else {
        mensaje.textContent = "No ha seleccionado ningún deporte.";
    }
}