function cargarTemperaturas() {
  const lista = [];
  for (let i = 0; i < 6; i++) {
    const tem = parseInt(prompt(`Ingrese la temperatura n°${i + 1} de las últimas 6 horas :`));
    lista.push(tem);
  }
  return lista;
}

function mayorYMenor(lista) {
  let men = lista[0];
  let may = lista[0];

  for (const elemento of lista) {
    if (elemento > may) {
      may = elemento;
    } else if (elemento < men) {
      men = elemento;
    }
  }
  return [may, men]; 
}


function imprimir(extremos) {
  console.log("--- La mayor y menor temperatura de las últimas 6 horas ---");
  const [may, men] = extremos; 
  console.log("El valor mayor de las temperaturas es : ", may);
  console.log("El valor menor de las temperaturas es : ", men);
}

function bloquePrincipal() {
  const lista = cargarTemperaturas();
  const extremos = mayorYMenor(lista);
  imprimir(extremos);
}

bloquePrincipal();