function OP1(Peticiones,id) {
    // referencia acerca al botón
const Op1 = document.getElementById(id);

// maneja eventos al botón
Op1.addEventListener("click", function() {
  // redirección
  window.location.href = "http://127.0.0.1:8000/"+Peticiones;
});
}

function Del(){
  
  fetch('http://127.0.0.1:5000/BorrarBase', {
    method: 'GET',
    headers: {}
  })
  .then(response => response.text())
  .then(data => {
    alert(data)
  })
  .catch(error => console.error(error));
  
}
