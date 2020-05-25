document.getElementById('user').addEventListener('submit', performPostRequest);
  function performPostRequest(e) {
    var email = document.getElementById('eml_usuario').value;
    var password = document.getElementById('psw_usuario').value;

    
    axios.post('http://127.0.0.1:5000/api/v1/insert/usuarios', {
      eml_usuario: email,
      psw_usuario: password
    })
    .then(function (response) {
        console.log(response);
    })
    .catch(function (error) {
      if(error == null){
          console.log("email ou senha errado")
      }
    });
    
    e.preventDefault();
  }

