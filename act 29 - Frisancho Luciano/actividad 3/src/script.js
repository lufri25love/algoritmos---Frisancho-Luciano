/*
Ejercicio 3: Borrador de Notas de Sesión
Enunciado: Crear una aplicación de notas rápidas que permita al usuario escribir un
mensaje o nota en un campo de texto y guardarlo de forma temporal utilizando
SessionStorage.
 Debe contar con un campo de texto (&lt;textarea&gt; o &lt;input&gt;) y un botón &quot;Guardar
Nota&quot;.
 Al hacer clic en el botón &quot;Guardar Nota&quot;, el texto ingresado debe almacenarse
en SessionStorage y mostrarse en un elemento dentro del DOM (por ejemplo,
en un contenedor &lt;div&gt; o párrafo).
 Al recargar la página (F5), la nota guardada debe recuperarse de
SessionStorage y seguir mostrándose en pantalla.
 Debe incluir un botón &quot;Borrar Nota&quot; que elimine el registro de SessionStorage
mediante removeItem() y limpie el contenido del DOM.
*/

window.onload = function() {
    cargarNota();
};

function guardarNota() {
    let texto = document.getElementById("notaInput").value;

    if (texto !== "") {

        sessionStorage.setItem("notaSesion", texto);
        

        cargarNota();
    } else {
        alert("Por favor, ingrese un texto antes de guardar.");
    }
}

function cargarNota() {
    let notaGuardada = sessionStorage.getItem("notaSesion");
    let contenedor = document.getElementById("contenedorNota");
    let input = document.getElementById("notaInput");

    if (notaGuardada !== null) {
        contenedor.textContent = notaGuardada;
        input.value = notaGuardada;
    } else {
        contenedor.textContent = "No hay notas guardadas.";
        input.value = "";
    }
}

function borrarNota() {

    sessionStorage.removeItem("notaSesion");

    cargarNota();
}