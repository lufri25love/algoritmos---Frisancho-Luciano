/*
5. Generar un presupuesto de un equipo de computación a partir de tres
objetos de tipo SELECT que nos permiten seleccionar:
Procesador (Intel I3 - $400, Intel I5 $600, Intel I7 $800).
Monitor (Samsung 20' - $250, Samsung 22' - $350, Samsung 26' - $550)
Disco Duro(500 Gb - $300, 1 Tb - $440, 3 Tb - $500)
Para cada característica indicamos string a mostrar (Ej. Intel I3) y el
valor asociado a dicho string (Ej. 400).
Al presionar un botón "Calcular" mostrar el presupuesto en un objeto de
tipo TEXT.
*/

function calcularPresupuesto() {
    let precioProcesador = parseInt(document.getElementById("procesador").value);
    let precioMonitor = parseInt(document.getElementById("monitor").value);
    let precioDisco = parseInt(document.getElementById("disco").value);

    let total = precioProcesador + precioMonitor + precioDisco;

    let inputTotal = document.getElementById("total");
    inputTotal.value = "$" + total;
}