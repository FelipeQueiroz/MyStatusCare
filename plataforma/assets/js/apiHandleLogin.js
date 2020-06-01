document.getElementById('user').addEventListener('submit', performPostRequest);
  function performPostRequest(e) {
    var email = document.getElementById('eml_usuario').value;
    var password = document.getElementById('psw_usuario').value;

    
    axios.post('http://localhost/api/v1/login', {
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
  function onSignIn(googleUser) {

    // Useful data for your client-side scripts:
    var profile = googleUser.getBasicProfile();
     // Don't send this directly to your server!
    console.log('Full Name: ' + profile.getName());
    console.log('Given Name: ' + profile.getGivenName());
    console.log('Family Name: ' + profile.getFamilyName());
    console.log("Image URL: " + profile.getImageUrl());

    // The ID token you need to pass to your backend:
    var id_token = googleUser.getAuthResponse().id_token;
    console.log("ID Token: " + id_token);
  }
  function onSuccess(googleUser) {
    console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
    console.log("Email: " + profile.getBasicProfile().getEmail());
    console.log("ID: " + profile.getBasicProfile().getId());
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
    
