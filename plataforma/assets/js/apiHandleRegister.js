//Função para mostrar cidades no formulário
function getCities (){

  const select = document.getElementById('cod_cidade');

  axios.get('http://127.0.0.1:5000/api/v1/cidade/all').then(response => {
    this.infos = response.data;
    for(var i = 0; i < infos.length; i++){
      
      var opt = document.createElement('option');

      array = Object.entries(infos[i]);
      cidade = array[2].join();
      valor = array[1].join();
      
      opt.value += valor.replace(/idt_cidade,/, '');
      opt.innerHTML += cidade.replace(/nme_cidade,/, '');
      select.appendChild(opt);
    }
    
  });
};



document.getElementById('user').addEventListener('submit', performPostRequest);


  function performPostRequest(e) {
    var user = document.getElementById('nme_usuario').value;
    var email = document.getElementById('eml_usuario').value;
    var cidade = document.getElementById('cod_cidade').value;
    var idade = document.getElementById('ida_usuario').value;
    var endereco = document.getElementById('end_usuario').value;
    var password = document.getElementById('psw_usuario').value;
    var userArray = new Array(user,email,endereco);

    
    axios.post('http://127.0.0.1:5000/api/v1/insert/usuarios', {
      nme_usuario: user,
      eml_usuario: email,
      end_usuario: endereco,
      psw_usuario: password,
      cod_cidade: cidade,
      ida_cidade: idade
      
    })
    .then(function (response) {
      console.log(response);
      window.location.href = "../plataforma/index.html"
    })
    .catch(function (error) {
      var errorInput = document.getElementById('errorAlert');
      errorInput.style.display = "initial";
      errorInput.innerHTML += error;
      console.log(error);
    });
    
    e.preventDefault();
  }

