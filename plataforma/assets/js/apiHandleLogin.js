

  function onSuccess(googleUser) {
    sessionStorage.setItem('name',googleUser.getBasicProfile().getName());
    sessionStorage.setItem('email', googleUser.getBasicProfile().getEmail());
    sessionStorage.setItem('id',googleUser.getBasicProfile().getId());
    if(isRegister() == false){
     window.location.href = "../plataforma/register.html";
    } else{
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
    axios.post('http://192.168.1.222/api/v1/login', {
      eml_usuario: sessionStorage.getItem('email'),
      idt_usuario: sessionStorage.getItem('id')
    })
    .then(function (response) {
      console.log(response);
      return true;
    })
    .catch(function (error) {
      console.log(error);
      return false;
    });
  }
