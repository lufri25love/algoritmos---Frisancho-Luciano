/*
2. Cargar un nombre y un apellido en dos text. Al presionar un botón,
concatenarlos y mostrarlos en un tercer text (Tener en cuenta que
podemos modificar la propiedad value de un objeto TEXT cuando ocurre
un evento).
*/
function verificar(){
    let nombre = document.getElementById("clave1").value;
    let apellido = document.getElementById("clave2").value;
    document.getElementById("texto_completo").textContent = `${nombre} ${apellido}`
}