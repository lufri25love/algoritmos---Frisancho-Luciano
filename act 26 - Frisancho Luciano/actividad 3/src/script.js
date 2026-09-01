/*
Ejercicio 03: Simulador de Votación en Línea
Plantear una página con 3 botones, cada uno representando un candidato distinto.
Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
candidato y mostrar el total actualizado en pantalla.
Además:
- El sistema debe mostrar en consola quién va ganando cada vez que se registra un voto.
- Si hay un empate, debe mostrar el mensaje "Hay un empate".
*/
let votosA = 0;
let votosB = 0;
let votosC = 0;

function votarA() {
    votosA++;
    let contadorA = document.getElementById("votosA");
    contadorA.textContent = votosA;
    verificarGanador();
}
function votarB() {
    votosB++;
    let contadorB = document.getElementById("votosB");
    contadorB.textContent = votosB;
    verificarGanador();
}
function votarC() {
    votosC++;
    let contadorC = document.getElementById("votosC");
    contadorC.textContent = votosC;
    verificarGanador();
}
function verificarGanador() {
    if (votosA > votosB && votosA > votosC) {
        console.log("Va ganando el Candidato A");
    } else if (votosB > votosA && votosB > votosC) {
        console.log("Va ganando el Candidato B");
    } else if (votosC > votosA && votosC > votosB) {
        console.log("Va ganando el Candidato C");
    } else {
        console.log("Hay un empate");
    }
}