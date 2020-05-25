document.getElementById('page-top').addEventListener("load", onLoad);

var username = document.getElementById('userName');
var userNav = document.getElementById('nav-link');
var pontuacao = document.getElementById('pto_usuario');

function onLoad(e){
    axios.get("http://127.0.0.1:5000/api/v1/resources/usuarios?idt_usuario=" + localStorage.id)
    .then(function (response) {
      username.innerHTML += " " + response.data[0].nme_usuario + " !";
      userNav.innerHTML += " " + response.data[0].nme_usuario;
      pontuacao.innerHTML += " " + response.data[0].pto_usuario;
      console.log(response.data[0].nme_usuario)
    })

}




if (sessionStorage.getItem('AuthenticationState') === null) {
  window.open("AccessDenied.html", "_self");
}
else if (Date.now > new Date(sessionStorage.getItem('AuthenticationExpires'))) {
     window.open("AccessDenied.html", "_self");
}
else {}