// Grafica
const graph = document.getElementById('info_graphs');
const url = 'http://127.0.0.1:5000/';

var autorizaciones = {};
var facturas = {};
graph.onclick = function () {
    var fechas = [];
    const dropdown = document.getElementById('mydropdown');
    const dropdown2 = document.getElementById('mydropdown2');
    const dropdown3 = document.getElementById('mydropdown3');
    (async () => {
        const rawResponse = await fetch(url + 'get-dict', {
            method: 'GET'
        });
        const content = await rawResponse.json();
        if(content.message == "True"){
            autorizaciones = content.autorizaciones;
            facturas = content.facturas;
            for(i = 0; i < autorizaciones.length; i++){
                fechas.push(autorizaciones[i].autorizacion.fecha);
            }
            for(var i in fechas){
                var opt = document.createElement("option");
                opt.value = fechas[i];
                opt.text = fechas[i];
    
                dropdown.appendChild(opt);
            }
            for(var i in fechas){
                var opt = document.createElement("option");
                opt.value = fechas[i];
                opt.text = fechas[i];
    
                dropdown2.appendChild(opt);
            }
            for(var i in fechas){
                var opt = document.createElement("option");
                opt.value = fechas[i];
                opt.text = fechas[i];
    
                dropdown3.appendChild(opt);
            }
            alert("Informacion obtenida.");
        }else{
            alert("No hay informacion");
        }
    })();
}

const reporte = document.getElementById('reporte');
reporte.onclick = function() {
    var doc = new jsPDF();
    var elementHTML = $('#content').html();
    var specialElementHandlers = {
        '#elementH': function (element, renderer) {
            return true;
        }
    };
    doc.fromHTML(elementHTML, 15, 15, {
        'width': 1000,
        'elementHandlers': specialElementHandlers
    });
    
    // Save the PDF
    doc.save('sample-document.pdf');
}

// Grafica 1
const btngraph1 = document.getElementById('btn_graph1');
let myChart;
btngraph1.onclick = function () {
    const fecha = document.getElementById('mydropdown').value;
    if (fecha == 'starter'){
        alert("Debe seleccionar una fecha.")
    }
    else{
        var lbl = [];
        var emitido = [];
        var recibido = [];
        for (i = 0; i < autorizaciones.length; i++){
            if (fecha == autorizaciones[i].autorizacion.fecha){
                for (j = 0; j < autorizaciones[i].autorizacion.aprobaciones.length; j++){
                    if(lbl.includes(autorizaciones[i].autorizacion.aprobaciones[j].aprobacion.emisor) == false){
                        lbl.push(autorizaciones[i].autorizacion.aprobaciones[j].aprobacion.emisor)                        
                    }
                }
                for (k = 0; k < lbl.length; k++){
                    var contribuido = 0;
                    for(z = 0; z < facturas.length; z++){
                        if(fecha == facturas[z].tiempo && lbl[k] == facturas[z].nit_emisor){
                            contribuido += facturas[z].iva;
                        }
                    }
                    emitido.push(contribuido);
                }
                for (a = 0; a < lbl.length; a++){
                    var sacado = 0;
                    for(b = 0; b < facturas.length; b++){
                        if(fecha == facturas[b].tiempo && lbl[a] == facturas[b].nit_receptor){
                            sacado += facturas[b].iva;
                        }
                    }
                    recibido.push(sacado);
                }
            }
        }
        const ctx = document.getElementById('myChart1');
        if (myChart){
            myChart.destroy();
        }
        myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: lbl,
                datasets: [{
                    label: 'Emitido',
                    data: emitido,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 0.2)'
                    ],
                    borderWidth: 1
                }, {
                    label: 'Recibido',
                    data: recibido,
                    backgroundColor: [
                        'rgba(20, 143, 119, 0.2)'  
                    ],
                    borderColor: [
                        'rgba(20, 143, 119, 0.2)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });   
    }
} 
