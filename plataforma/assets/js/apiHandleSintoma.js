
var selectSintomas = document.getElementById("selectSintomas");
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
        var sintoma = document.getElementById('selectSintomas').value;
        var dtaSintoma = document.getElementById('dataSintoma').value;
        axios.post("http://127.0.0.1:5000/api/v1/insert/sintoma?idt_usuario=" + localStorage.id,{
            idt_sintoma: sintoma,
            dta_sintoma: dtaSintoma
        })
        .then(function(response){
            console.log(response)
            window.location.reload();
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
              cell2.innerHTML = response.data[i].dta_sintoma;
              table.appendChild(row);
            }
            
          });
      
};