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
  console.log("-----------------------------------");
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
  console.log("--------------------------------------");
}

// Bloque Principal
function bloquePrincipal() {
  const lista = cargarDatos();
  imprimir(lista);
  filtro(lista);
}

bloquePrincipal();