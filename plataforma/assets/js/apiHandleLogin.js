

  function onSuccess(googleUser) {
    sessionStorage.setItem('name',googleUser.getBasicProfile().getName());
    sessionStorage.setItem('email', googleUser.getBasicProfile().getEmail());
    sessionStorage.setItem('idg',googleUser.getBasicProfile().getId());
    if(!isRegister()){
     window.location.href = "../plataforma/register.html";
    } else if(isRegister()){
      sessionStorage.setItem("AuthenticationState", "Authenticated");
      
      window.location.href = "../plataforma/index.html";
    }
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




  function isRegister(){
    axios.post('https://api-msc.educatux.com.br//api/v1/login', {
        eml_usuario: sessionStorage.getItem('email'),
        idg_usuario: sessionStorage.getItem('idg')
      }
    )
    .then(() => {return true})
    .catch(() => {return false});
  }
