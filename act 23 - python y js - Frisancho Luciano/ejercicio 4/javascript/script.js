/*
Ejercicio 4: Algoritmo de Compresión de Texto (RLE)
Contexto: En telecomunicaciones se utiliza el algoritmo Run-Length Encoding (RLE) para
comprimir secuencias de caracteres repetidos y ahorrar ancho de banda.
Consigna: Escribir la función comprimir_rle(texto) que reciba una cadena de caracteres en
mayúsculas y devuelva su versión comprimida.
Requisitos:
● Contar las apariciones consecutivas de cada carácter.
● Construir una cadena resultante intercalando el carácter con su cantidad de
apariciones consecutivas.
Ejemplo de Entrada: &quot;AAABBCDDDD&quot; Salida Esperada: &quot;A3B2C1D4&quot;
*/


function comprimir_rle(){
    let resultado = ""
    let contador = 1

    for(let i=0; i<(texto.length); i++ ){
        if (texto.slice(i) == texto.slice(i+1)){
            contador = contador + 1;
        }  
        else{
            resultado = resultado + texto.slice(i) + contador;
            contador = 1;
        }      
    resultado = resultado + texto.slice(contador) + contador;
    return resultado;
    }    
}


let texto = prompt("Ingrese un texto: ");
console.log("Texto original:", texto);
console.log("Texto comprimido:" + comprimir_rle());