  function isRegister(){
    axios.post('http://127.0.0.1:5000/api/v1/login', {
      eml_usuario: email,
      psw_usuario: password
    })
    .then(function (response) {
      return true;
    })
    .catch(function (error) {
      return false;
    });
  }

  function onSuccess(googleUser) {
    if(isRegister() == false){
    sessionStorage.setItem('name',googleUser.getBasicProfile().getName());
    sessionStorage.setItem('email', googleUser.getBasicProfile().getEmail());
    sessionStorage.setItem('id',googleUser.getBasicProfile().getId());
      window.location.href = "../plataforma/register.html";
    } else{
      localStorage.id = googleUser.getBasicProfile().getId();
      window.location.href= "../plataforma/index.html";
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
    
