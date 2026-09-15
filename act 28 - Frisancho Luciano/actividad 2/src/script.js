/*2. Confeccionar una página de visitas a un sitio, solicitar ingresar el nombre de una
persona, su mail y los comentarios (TEXTAREA). Mostrar luego llamando a la función
alert los datos ingresados. */

function Resultado(){
    let nombre=document.getElementById('nombre').value;
    let apellido=document.getElementById('apellido').value;
    let comentarios=document.getElementById('comentarios').value;
    alert('Valores ingresados; '+ nombre+ ', '+ apellido+ ', '+ comentarios)
}