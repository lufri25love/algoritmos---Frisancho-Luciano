/*
Ejercicio 2: Detector de Transacciones Sospechosas (Parseo)
Contexto: Un banco recibe un lote diario de movimientos en un único texto largo con el
formato &quot;ID:TIPO:MONTO&quot;, donde TIPO puede ser I (Ingreso) o E (Egreso), separados por
comas.
Consigna: Crear una función procesar_transacciones(cadena_texto) que reciba el texto de
movimientos y realice el procesamiento completo.
Requisitos:
● Parsear la cadena de texto separando cada registro.
● Calcular y retornar el balance total de la cuenta (Ingresos suman, Egresos restan).
● Generar y retornar una lista con los IDs de las transacciones consideradas
&quot;sospechosas&quot;. Una transacción es sospechosa si es un Egreso superior a
$50.000.
Ejemplo de Entrada: TX101:I:120000, TX102:E:15000, TX103:E:85000,
TX104:I:3000 Salida Esperada:
● Balance final: $23.000
● Transacciones sospechosas: [&#39;TX103&#39;]
*/

function procesar_transacciones (cadena){
    let transacciones = cadena.split(",");
    let balance = 0 ;
    const sospechosas = [];

    for (const i of transacciones){
        let datos = i.split(":");
        const id = datos[0];
        const tipo = datos[1];
        const monto = parseInt(datos[2]);

        if (tipo == "i"){
            balance = balance + monto;
        }
        if (tipo == "e"){
                balance = balance - monto;
            if (monto >= 50000){
                sospechosas.push(id)
            }
     
        }

    }
    return balance,sospechosas;
}

let cadena = prompt("ingrese las transacciones : ");

const [balance, sospechosas] = procesar_transacciones(cadena);

console.log("balance final : $");
console.log(balance);
console.log("transacciones sospechosas : ");
console.log(sospechosas);
