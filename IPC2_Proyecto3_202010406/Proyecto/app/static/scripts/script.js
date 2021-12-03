
const fileSelector = document.getElementById('my_file');
const url = 'http://127.0.0.1:5000/';

// Enviando archivo a backend
fileSelector.addEventListener('change', (Event)=>{
    const file = Event.target.files[0];
    // Parte para escribir texto de xml en cuadro entrada
    const text_area = document.getElementById('entrada');
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        text_area.innerHTML = reader.result;
    }, false);

    if (file){
        reader.readAsText(file);
    }
});

// Enviando info de entrada al presionar enviar
const send = document.getElementById('send');
var cont_salida = '';
send.onclick = function () {
    const text_area = document.getElementById('entrada').value;

    if (text_area != ''){
        (async () => {
            const rawResponse = await fetch(url + 'cargar-archivo', {
              method: 'POST',
              body: text_area
            });
            const content = await rawResponse.text();
            cont_salida = content;
            // console.log(content);
          })();
    } else {
        alert("Debe cargar un archivo primero");
    }

}

// Borrando archivo de base de datos
const del = document.getElementById('delete');
del.onclick = function () {
    const text_area = document.getElementById('entrada');
    const salida = document.getElementById('salida');
    (async () => {
        const rawResponse = await fetch(url + 'delete-file', {
            method: 'DELETE',
            body: ''
        });
        const content = await rawResponse.text();
        res = JSON.parse(content);
        if (res.message == 'FALSE'){
            alert('No existe una base de datos.');
        }else{
            text_area.innerHTML = '';
            salida.innerHTML = '';
            cont_salida = '';   
            alert('Base de datos eliminada');
        }

    })();
}

// Consultar Datos
const con_datos = document.getElementById('consulta');
con_datos.onclick = function() {
    const salida = document.getElementById('salida');
    (async () => {
        const rawResponse = await fetch(url + 'get-info', {
            method: 'GET'
        });
        const content = await rawResponse.text();
        res = JSON.parse(content);
        if (res.message == 'True'){
            salida.innerHTML = res.contenido;
        }else{
            alert('No hay informacion en la base de datos.');
        }
    })();
}