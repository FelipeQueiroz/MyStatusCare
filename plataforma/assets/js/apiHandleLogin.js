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
  function (googleUser) {

          // Useful data for your client-side scripts:
          var profile = googleUser.getBasicProfile();
          console.log("ID: " + profile.getId()); // Don't send this directly to your server!
          console.log('Full Name: ' + profile.getName());
          console.log('Given Name: ' + profile.getGivenName());
          console.log('Family Name: ' + profile.getFamilyName());
          console.log("Image URL: " + profile.getImageUrl());
          console.log("Email: " + profile.getEmail());
  
          // The ID token you need to pass to your backend:
          var id_token = googleUser.getAuthResponse().id_token;
          console.log("ID Token: " + id_token);
        }
  
