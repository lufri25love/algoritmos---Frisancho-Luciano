/*
Ejercicio 04: Lista de Compras Dinámica
Confeccionar una página con un campo de texto y un botón “Agregar”.
Cada vez que se presione el botón, el producto ingresado en el campo debe añadirse
a una lista (<ul>).
Además:
- La lista debe permitir eliminar un producto haciendo clic sobre él.
- En consola debe mostrarse en todo momento la cantidad de productos actuales en la lista.
*/

function agregarProducto() {
    let input = document.getElementById("productoInput");
    let textoProducto = input.value;
    if (textoProducto !== "") {
        let lista = document.getElementById("listaProductos");
        let nuevoItem = document.createElement("li");
        nuevoItem.textContent = textoProducto;
        nuevoItem.onclick = function() {
            nuevoItem.remove();
            mostrarCantidadProductos();
        };
        lista.appendChild(nuevoItem);
        input.value = "";
        mostrarCantidadProductos();
    }
}

function mostrarCantidadProductos() {
    let lista = document.getElementById("listaProductos");
    console.log("Cantidad total de productos en la lista:", lista.children.length);
}