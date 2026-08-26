/*
3-
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
 La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ [Franco, (78.5, 77.2, 79.1)], [Lewis, (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece.
*/
function cargarPilotos() {
  const pilotos = [];
  
  for (let i = 0; i < 4; i++) {
    const nombre = prompt(`Ingrese el nombre del piloto n° ${i + 1}:`);
    const vue1 = parseFloat(prompt(`Ingrese el tiempo de la 1° vuelta de ${nombre}:`));
    const vue2 = parseFloat(prompt(`Ingrese el tiempo de la 2° vuelta de ${nombre}:`));
    const vue3 = parseFloat(prompt(`Ingrese el tiempo de la 3° vuelta de ${nombre}:`));
    
    pilotos.push([nombre, [vue1, vue2, vue3]]);
  }
  return pilotos;
}

// 2. Calcular Promedios
function calcularPromedios(pilotos) {
  console.log("------ Promedio de tiempo por piloto ------");
  for (const [nombre, tiempos] of pilotos) {
    let suma = 0;
    for (const tiempo of tiempos) {
      suma += tiempo;
    }
    const promedio = suma / tiempos.length;
    console.log(`El piloto ${nombre} tiene un tiempo promedio de: ${promedio.toFixed(2)}s`);
  }
  console.log("------------------------------------------");
}


function mejorVuelta(pilotos) {
  console.log("--------------- Mejor Vuelta ------------------")
  let mejorTiempo = pilotos[0][1][0]; 
  let mejorPiloto = pilotos[0][0];
  for (const [nombre, tiempos] of pilotos) {
    for (const tiempo of tiempos) {
      if (tiempo < mejorTiempo) {
        mejorTiempo = tiempo;
        mejorPiloto = nombre;
      }
    }
  }
  console.log(`La vuelta más rápida fue de ${mejorPiloto}, con un tiempo de: ${mejorTiempo}s`);
  console.log("-----------------------------------------------");
}

// Bloque Principal
function bloquePrincipal() {
  const pilotos = cargarPilotos();
  calcularPromedios(pilotos);
  mejorVuelta(pilotos);
}
bloquePrincipal();