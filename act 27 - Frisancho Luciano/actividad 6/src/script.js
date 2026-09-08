/*
6. Confeccionar una página que permita tomar un examen múltiple choice.
Se debe mostrar una pregunta y seguidamente un objeto SELECT con
las respuestas posibles. Al presionar un botón mostrar la cantidad de
respuestas correctas e incorrectas (Disponer 4 preguntas y sus
respectivos controles SELECT).
*/

function evaluarExamen() {
    let correctas = 0;
    let incorrectas = 0;
    let p1 = document.getElementById("p1").value;
    let p2 = document.getElementById("p2").value;
    let p3 = document.getElementById("p3").value;
    let p4 = document.getElementById("p4").value;
    let respuestas = [p1, p2, p3, p4];
    for (let i = 0; i < respuestas.length; i++) {
        if (respuestas[i] === "correcto") {
            correctas++;
        } else if (respuestas[i] === "incorrecto") {
            incorrectas++;
        }
    }
    let mensaje = document.getElementById("resultado");
    mensaje.textContent = `Respuestas correctas: ${correctas} | Respuestas incorrectas: ${incorrectas}`;
}