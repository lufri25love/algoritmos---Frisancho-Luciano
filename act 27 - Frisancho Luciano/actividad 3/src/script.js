/*
3. Disponer dos campos de texto tipo password. Cuando se presione un
botón mostrar si las dos claves ingresadas son iguales o no (es muy
común solicitar al operador el ingreso de dos veces de su clave para
validar si las escribió correctamente, esto se hace cuando se crea una
password para el ingreso a un sitio o para el cambio de una existente).
Tener en cuenta que podemos emplear el operador == para ver si dos
string son iguales.
*/
function validar() {
    let contraseña = document.getElementById("contraseña").value;
    let confirmar = document.getElementById("confirmar").value;
    if (contraseña == confirmar) {
        alert("Las contraseñas son iguales.");
    } else {
        alert("Las contraseñas no coinciden.");
    }
}