/*
Ejercicio 05: Control de Temperatura
Diseñar una página con un campo de texto para ingresar una temperatura y un botón
“Verificar”.
Cuando el usuario haga clic:
- Si la temperatura es menor a 10, mostrar en el documento el mensaje “Hace frío” en azul.
- Si está entre 10 y 25, mostrar “Clima agradable” en verde.
- Si es mayor a 25, mostrar “Hace calor” en rojo.
Además, cada verificación debe registrarse en consola con la fecha y hora
exacta (usando Date()).
*/

function verificarTemperatura() {
    let input = document.getElementById("temperaturaInput");
    let resultado = document.getElementById("resultado");
    let valor = parseFloat(input.value);

    if (!isNaN(valor)) {
        if (valor < 10) {
            resultado.textContent = "Hace frío";
            resultado.style.color = "blue";
        } else if (valor >= 10 && valor <= 25) {
            resultado.textContent = "Clima agradable";
            resultado.style.color = "green";
        } else {
            resultado.textContent = "Hace calor";
            resultado.style.color = "red";
        }
        let fechaActual = new Date();
        console.log(`[${fechaActual.toLocaleString()}] Verificación realizada para ${valor}°C: "${resultado.textContent}"`);
    } else {
        resultado.textContent = "Por favor, ingrese una temperatura válida.";
        resultado.style.color = "black";
    }
}