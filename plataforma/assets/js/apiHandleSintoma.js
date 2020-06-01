
var selectSintomas = document.getElementById("select_sintoma");
axios.get('http://127.0.0.1:5000/api/v1/sintomas/all')
    .then(function (response) {
        for(var i = 0; i < response.data.length; i++){

            var opt = document.createElement('option');

            opt.value += response.data[i].idt_sintoma;
            opt.innerHTML += response.data[i].nme_sintoma;
            
        selectSintomas.appendChild(opt);
        }
    });

document.getElementById('addSintoma').addEventListener('submit', saveSintoma);

    function saveSintoma(e){
        var sintoma = document.getElementById('select_sintoma').value;
        var dtaSintoma = document.getElementById('dataSintoma').value;
        console.log(sintoma, dtaSintoma);
        axios.post("http://127.0.0.1:5000/api/v1/insert/sintoma?idt_usuario=" + localStorage.id,{
            idt_usuario: localStorage.id,
            idt_sintoma: sintoma,
            dta_sintoma: dtaSintoma
        })
        .then(function(response){
            console.log(response)
            window.location.href = "../plataforma/sintomas.html"
        })
        .catch(function(error){
            console.log(error)
        });

        e.preventDefault();
    }

    document.getElementById('addTemperatura').addEventListener('submit', saveTemperatura);

    function saveTemperatura(e){
        var valor = document.getElementById('valorTemperatura').value;
        var dtaTemperatura = document.getElementById('dataTemperatura').value;
        console.log(valor, dtaTemperatura);
        axios.post("http://127.0.0.1:5000/api/v1/insert/temperatura?idt_usuario=" + localStorage.id,{
            vlr_temperatura: valor,
            dta_temperatura: dtaTemperatura
        })
        .then(function(response){
            window.location.href = "../plataforma/sintomas.html"
        })
        .catch(function(error){
            console.log(error)
        });

        e.preventDefault();
    }

function loadSintomas(){

        const table = document.getElementById('tableRow');
        
          axios.get('http://127.0.0.1:5000/api/v1/resources/sintomas_usuario?idt_usuario=' + localStorage.id)
          .then(function (response){
            for(var i = 0; i < response.data.length; i++){
              
              var row = table.insertRow(0);
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
                
              cell1.innerHTML = response.data[i].nme_sintoma;
              cell2.innerHTML = moment(response.data[i].dta_sintoma).format("DD/MM/YYYY");
              table.appendChild(row);
            }
            
          });

          const tableTemp = document.getElementById('tableRowTemp');
        
          axios.get('http://127.0.0.1:5000/api/v1/resources/temperatura?idt_usuario=' + localStorage.id)
          .then(function (response){
            for(var i = 0; i < response.data.length; i++){
              
              var row = tableTemp.insertRow(0);
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
                
              cell1.innerHTML = response.data[i].vlr_temperatura;
              cell2.innerHTML = moment(response.data[i].dta_temperatura).format("DD/MM/YYYY");
              tableTemp.appendChild(row);
            }
            
          });
      
};