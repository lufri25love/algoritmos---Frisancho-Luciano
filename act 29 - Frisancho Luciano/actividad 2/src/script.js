/*
Ejercicio 2: Carrito de Compras con Conteo de Productos
Enunciado: Crear un carrito de compras utilizando LocalStorage, que permita a los
usuarios agregar productos y muestre la cantidad total de productos en el carrito.
1. Los productos deben tener un botón para agregar al carrito.
2. Al agregar un producto, se debe mostrar el número total de productos en el
carrito, almacenándolo en LocalStorage.
3. Al recargar la página, el número total de productos debe recuperarse de
LocalStorage y mostrarse correctamente.
*/

window.onload = function() {
    cargarCarrito();
};

function agregarAlCarrito() {
    let total = localStorage.getItem("cantidadCarrito");
    
    if (total === null) {
        total = 0;
    } else {
        total = parseInt(total);
    }
    total++;


    localStorage.setItem("cantidadCarrito", total);
    document.getElementById("contador").textContent = total;
}

function cargarCarrito() {
    let totalGuardado = localStorage.getItem("cantidadCarrito");
    if (totalGuardado !== null) {
        document.getElementById("contador").textContent = totalGuardado;
    } else {
        document.getElementById("contador").textContent = 0;
    }
}

function vaciarCarrito() {
    localStorage.removeItem("cantidadCarrito");
    document.getElementById("contador").textContent = 0;
}