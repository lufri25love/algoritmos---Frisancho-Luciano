function procesarTransacciones() {
    let suma = 0;
    let lista1 = [];
    let lista2 = [];
    let num = parseInt(prompt("¿Cuántas veces desea ingresar datos?"));
    for (let x = 0; x < num; x++) {
        let id = prompt("Ingrese el ID del movimiento:");
        let tipo = prompt("Ingrese el tipo (I/E):");
        let monto = parseInt(prompt("Ingrese el monto:"));
        lista1.push(id + ":" + tipo + ":" + monto);
        if (tipo == "I") {
            suma = suma + monto;
        } else if (tipo == "E") {
            suma = suma - monto;
        }
        if (tipo == "E" && monto > 50000) {
            lista2.push(id);
        }
    }

    console.log(lista1);
    console.log("Balance final: $" + suma);
    console.log("Transacciones sospechosas: " + lista2);
}
procesarTransacciones();