/*
Ejercicio 02: Creación Dinámica de Elementos y Eventos
Enunciado: Desarrollar un programa que permita a la persona agregar nuevos
elementos a una lista mediante un botón. Los pasos son:
1. Al hacer clic en un botón, se debe crear un nuevo elemento li en una lista ya
existente.
2. El contenido del nuevo elemento debe ser el texto: Nuevo Elemento.
3. Usar createElement() para crear el nuevo elemento y appendChild() para
añadirlo a la lista.
4. Cada vez que se agrega un nuevo elemento, se debe mostrar una alerta
indicando: Se ha añadido un nuevo elemento.
*/
function agregar() {
    let nuevoElemento = document.createElement("li");
    nuevoElemento.textContent = "nuevo elemento";
    alert("nuevo se ha añadido un nuevo elemento")
    document.getElementById("lista").appendChild(nuevoElemento);
}