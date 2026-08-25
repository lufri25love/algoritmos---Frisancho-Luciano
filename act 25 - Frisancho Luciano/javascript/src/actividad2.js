/*
Para un sistema de radares de tránsito, se necesita registrar la ubicación geográfica de 4
cámaras de control.
 Almacenar en una lista las coordenadas de las 4 cámaras. Cada elemento de la
lista debe ser una tupla de dos flotantes (latitud, longitud) ingresados por teclado.
Desarrollar las siguientes funciones:
1. Cargar coordenadas: Solicitar la latitud y la longitud de cada una de las 4
cámaras para armar las tuplas y agregarlas a la lista.
2. Listar posiciones: Recibir la lista e imprimir las coordenadas de todas las
cámaras. Importante: Realizar el recorrido utilizando un bucle for que
desempaquete la tupla directamente en las variables lat y lon en cada vuelta (sin
utilizar índices numéricos como [0] o [1]).
3. Filtrar hemisferio: Contar e informar cuántas de las cámaras se encuentran
ubicadas en el hemisferio norte (latitud mayor a cero).
*/

function cargarDatos() {
  const lista = [];
  for (let x = 0; x < 4; x++) {
    const latitud = parseFloat(prompt(`Ingrese la latitud de la cámara n° ${x + 1}:`));
    const longitud = parseFloat(prompt(`Ingrese la longitud de la cámara n° ${x + 1}:`));
    lista.push([latitud, longitud]); 
  }
  return lista;
}

function imprimir(lista) {
  console.log("------ Lista de las cámaras con su latitud y longitud ------");
  let i = 1;
  for (const [lat, lon] of lista) {
    console.log(`La cámara n° ${i} tiene latitud: ${lat} y longitud: ${lon}`);
    i++;
  }
  console.log("----------------------------------------------------------");
}

function filtro(lista) {
  console.log("------ Cámaras ubicadas en el hemisferio norte ------");
  let contadorNorte = 0;
  let i = 1;
  for (const [lat, lon] of lista) {
    if (lat > 0) {
      console.log(`La cámara n° ${i} se encuentra en el hemisferio norte (Latitud: ${lat})`);
      contadorNorte++;
    }
    i++;
  }

  console.log(`Total de cámaras en el hemisferio norte: ${contadorNorte}`);
  console.log("-----------------------------------------------------");
}

// Bloque Principal
function bloquePrincipal() {
  const lista = cargarDatos();
  imprimir(lista);
  filtro(lista);
}
bloquePrincipal();