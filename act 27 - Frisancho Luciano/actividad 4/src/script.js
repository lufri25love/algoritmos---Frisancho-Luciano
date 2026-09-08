/*
4. Confeccionar una página que muestre un objeto SELECT con distintos
tipos de pizzas (Jamón y Queso, Muzzarella, Morrones). Al seleccionar
una, mostrar en un objeto de tipo TEXT el precio de la misma.
*/

function bro_pizza_pls() {
    let select = document.getElementById("elliot");
    let inputPrecio = document.getElementById("precioInput");
    let precio = select.value;
    if (precio !== "") {
        inputPrecio.value = "$" + precio;
    } else {
        inputPrecio.value = "";
    }
}
