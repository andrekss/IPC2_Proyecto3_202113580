function Op1(solicitud,Post){
    fetch('http://127.0.0.1:5000/'+Post, {
        method: 'POST',
        body: solicitud,
        headers: {
          'Content-Type': 'application/xml'
        }
      })
      .then(response => response.text())
      .then(xml => {
        // hacer algo con la respuesta en formato XML
        alert(respuesta(xml))

      })
      .catch(error => console.error(error));
      
}

function leerArchivo(id) {
    // Obtener el archivo seleccionado por el usuario
    var file = document.getElementById(id).files[0];
  
    // Crear una instancia de FileReader
    var reader = new FileReader();
  
    // Definir la función que se ejecutará cuando se cargue el archivo
    reader.onload = function() {
      // Obtener el contenido del archivo
      var contenido = reader.result;
    if (id == 'op1'){
      Op1(contenido,'Configuracion')
    } else {
        Op1(contenido,'Mensajes') 
    }
    };
  
    // Leer el archivo como texto
    reader.readAsText(file);
  }