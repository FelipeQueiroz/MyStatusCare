function loadUser(){

var username = document.getElementById('username');
var email = document.getElementById('email');
var endereco = document.getElementById('endereco');

axios.get("http://192.168.1.222/api/v1/resources/usuarios?idt_usuario=" + localStorage.id)
.then(function (response) {
  username.placeholder += " " + response.data[0].nme_usuario;
  email.placeholder += " " + response.data[0].eml_usuario;
  endereco.placeholder += " " + response.data[0].end_usuario;
})

}

