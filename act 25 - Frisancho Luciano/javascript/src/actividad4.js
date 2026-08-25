/*
4-
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
*/

function cargarDatos() {
  const componentes = [];
  for (let i = 0; i < 5; i++) {
    const nombre = prompt(`Ingrese el nombre del artículo n° ${i + 1}:`);
    const precio = parseFloat(prompt(`Ingrese el precio del producto ${nombre}:`));
    const stock = parseInt(prompt(`Ingrese la cantidad en stock del producto ${nombre}:`));
    componentes.push([nombre, precio, stock]);
  }
  return componentes;
}


function imprimir(componentes) {
  console.log("------------- Lista de productos con su precio y stock -------------");
  for (const [nombre, precio, stock] of componentes) {
    console.log(`El producto ${nombre} tiene un precio de $${precio} y un stock de ${stock} unidades.`);
  }
}
function inventarioTotal(componentes) {
  console.log("----------------- Monto total del inventario -----------------");
  let suma = 0;
  for (const [, precio, stock] of componentes) {
    suma += precio * stock;
  }
  console.log(`El valor total de la mercadería en el local es: $${suma}`);
}

function alerta(componentes) {
  console.log("---------- Alerta: Productos con stock menor o igual a 10 ----------");
  let hayAlertas = false;
  for (const [nombre, , stock] of componentes) {
    if (stock <= 10) {
      console.log(` ${nombre} Stock actual: ${stock}`);
      hayAlertas = true;
    }
  }
  if (!hayAlertas) {
    console.log("Todos los productos cuentan con stock suficiente.");
  }
}

// Bloque Principal
function bloquePrincipal() {
  const componentes = cargarDatos();
  imprimir(componentes);
  inventarioTotal(componentes);
  alerta(componentes);
}
bloquePrincipal();