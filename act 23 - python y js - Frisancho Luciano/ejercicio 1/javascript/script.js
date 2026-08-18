const ReservaCine = {

    reservarConsecutivos: function(sala, fila, cantidad) {
        const columnas = sala[fila].length;
        for (let inicio = 0; inicio <= columnas - cantidad; inicio++) {
            let disponibles = true;
            for (let i = inicio; i < inicio + cantidad; i++) {
                if (sala[fila][i] === 1) {
                    disponibles = false;
                    break;
                }
            }
            if (disponibles) {
                let columnasReservadas = [];
                for (let i = inicio; i < inicio + cantidad; i++) {
                    sala[fila][i] = 1;
                    columnasReservadas.push(i);
                }
                return `Reserva realizada. Columnas asignadas: ${columnasReservadas.join(", ")}`;
            }
        }
        return "No fue posible realizar la reserva.";
    }

};
const sala = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0]
];
console.log("Estado inicial:");
console.log(sala);
const resultado = ReservaCine.reservarConsecutivos(sala, 0, 3);
console.log(resultado);
console.log("Estado final:");
console.log(sala);