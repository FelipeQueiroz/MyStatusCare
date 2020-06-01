document.getElementById('user').addEventListener('submit', performPostRequest);
  function performPostRequest(e) {
    var email = document.getElementById('eml_usuario').value;
    var password = document.getElementById('psw_usuario').value;

    
    axios.post('http://127.0.0.1:5000/api/v1/login', {
      eml_usuario: email,
      psw_usuario: password
    })
    .then(function (response) {
      localStorage.id = response.data.idt_usuario;
      sessionStorage.setItem("AuthenticationState", "Authenticated");
      window.location.href = "../plataforma/index.html"
    })
    .catch(function (error) {
      var alert = document.getElementById("alert");
      alert.style.display = "block";
      alert.innerHTML = "Email ou senha incorreto";
    });
    
    e.preventDefault();
  }
  function onSuccess(googleUser) {
    sessionStorage.setItem('name',googleUser.getBasicProfile().getName());
    sessionStorage.setItem('email', googleUser.getBasicProfile().getEmail());
    sessionStorage.setItem('id',googleUser.getBasicProfile().getId());
    window.location.href = "../plataforma/register.html";
  }
  function onFailure(error) {
    console.log(error);
  }
  function renderButton() {
    gapi.signin2.render('my-signin2', {
      'scope': 'profile email',
      'width': 300,
      'height': 50,   
      'border-radius': 5,
      'longtitle': true,
      'theme': 'dark',
      'onsuccess': onSuccess,
      'onfailure': onFailure
    });
  }
    
