document.getElementById('user').addEventListener('submit', performPostRequest);
  function performPostRequest(e) {
    var user = document.getElementById('nme_usuario').value;
    var email = document.getElementById('eml_usuario').value;
    var endereco = document.getElementById('end_usuario').value;
    var password = document.getElementById('psw_usuario').value;

    
    axios.post('http://127.0.0.1:5000/api/v1/insert/usuarios', {
      nme_usuario: user,
      eml_usuario: email,
      end_usuario: endereco,
      psw_usuario: password
      
    })
    .then(function (response) {
      window.location.href = "../plataforma/index.html";
      
     console.log(response);
    })
    .catch(function (error) {
      var errorInput = document.getElementById('errorAlert');
      errorInput.style.display = "initial";
      errorInput.innerHTML == error;
    });
    
    e.preventDefault();
  }


