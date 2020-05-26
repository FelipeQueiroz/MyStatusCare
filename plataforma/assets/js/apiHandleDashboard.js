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
      var pont = response.data[0].pto_usuario;
      //Grafico da clasificação de risco
      var ctxD = document.getElementById("ptoChart").getContext('2d');
      var myLineChart = new Chart(ctxD, {
      type: 'doughnut',
      data: {
      labels: ["Pontuação"],
      datasets: [{
      
      data: [pont, (5 - pont)],
      backgroundColor: [ "#46BFBD", "#F7464A"],
      hoverBackgroundColor: ["#5AD3D1", "#FF5A5E"]
      }]
      },
      options: {
      responsive: true
      }
      });

    })

}




if (sessionStorage.getItem('AuthenticationState') === null) {
  window.open("AccessDenied.html", "_self");
}
else if (Date.now > new Date(sessionStorage.getItem('AuthenticationExpires'))) {
     window.open("AccessDenied.html", "_self");
}
else {}