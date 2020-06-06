//Função para mostrar cidades no formulário
function getCities (){

  const select = document.getElementById('cod_cidade');

  axios.get('https://api-msc.educatux.com.br/api/v1/cidade/all').then(response => {
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

var user = document.getElementById('nme_usuario');
var email = document.getElementById('eml_usuario');
user.value = sessionStorage.getItem('name');
email.value = sessionStorage.getItem('email');

  function performPostRequest(e) {
    var cidade = document.getElementById('cod_cidade').value;
    var idade = document.getElementById('ida_usuario').value;
    var endereco = document.getElementById('end_usuario').value;
    

    
    axios.post('https://api-msc.educatux.com.br/api/v1/insert/usuarios', {
      idg_usuario: sessionStorage.getItem('idg'),
      nme_usuario: user,
      eml_usuario: email,
      end_usuario: endereco,
      cod_cidade: cidade,
      ida_usuario: idade
      
    })
    .then(function (response) {
      window.location.href = "../plataforma/index.html";
    })
    .catch(function (error) {
      var errorInput = document.getElementById('errorAlert');
      errorInput.style.display = "initial";
      errorInput.innerHTML += error;
    });
    
    e.preventDefault();
  }

