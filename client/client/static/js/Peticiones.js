function regresar(){

  const Op1 = document.getElementById("op7");

  // maneja eventos al botón
  Op1.addEventListener("click", function() {
    // redirección
    window.location.href = "http://127.0.0.1:8000";
  });

}


function GetTablas(get){
    fetch('http://127.0.0.1:5000/'+get, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/xml'
      }
    })
    .then(response => response.text())
    .then(data => {
      // hacer algo con la respuesta en formato JSON
      document.getElementById('Tablas').innerHTML = data;
      //redirección('/MensajesUsuarios',false,data) // redirecciona a las tablas
    })
    .catch(error => console.error(error));
    
}

function Op1(solicitud,Post){  // solicitud lo que le enviemos y post el lugar de este
    fetch('http://127.0.0.1:5000/'+Post, {
        method: 'POST',
        body: solicitud,
        headers: {
          'Content-Type': 'application/text'
        }
      })
      .then(response => response.text())
      .then(data => {
        // hacer algo con la respuesta en formato XML
        document.getElementById('Tablas').innerHTML = data;
        //alert(respuesta(xml))

      })
      .catch(error => console.error(error));
      
}



function ObtenerUsuario(Post,id){
  var input = document.getElementById(id);

  var valor = input.value;

  Op1(valor,Post)
}


function OP1(Peticiones,id) {
  // referencia acerca al botón
const Op1 = document.getElementById(id);

// maneja eventos al botón
Op1.addEventListener("click", function() {
// redirección
window.location.href = "http://127.0.0.1:8000/"+Peticiones;
});
}





