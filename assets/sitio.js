// Botones para abrir o cerrar todas las respuestas del banco de preguntas.
document.addEventListener("DOMContentLoaded", function () {
  var abrir = document.getElementById("abrir-todas");
  var cerrar = document.getElementById("cerrar-todas");
  var respuestas = document.querySelectorAll("details.respuesta");

  function fijar(estado) {
    respuestas.forEach(function (d) { d.open = estado; });
  }

  if (abrir) abrir.addEventListener("click", function () { fijar(true); });
  if (cerrar) cerrar.addEventListener("click", function () { fijar(false); });

  // Si la dirección apunta a una respuesta (#r12), se abre al cargar.
  if (location.hash && location.hash.indexOf("#r") === 0) {
    var d = document.querySelector(location.hash);
    if (d && d.tagName === "DETAILS") d.open = true;
  }
});
