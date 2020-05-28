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
      var span = document.getElementById('risco');
      if(pont <= 3){
        span.innerHTML += " Estável"
      } else if (pont <= 5){
        span.innerHTML += " Preocupante"
      } else if (pont <= 8){
        span.innerHTML += " Vá para o hospital"
      }
      //Grafico da clasificação de risco
      var ctxD = document.getElementById("ptoChart").getContext('2d');
      var myLineChart = new Chart(ctxD, {
      

      type:"doughnut",
      data:{
        labels:["Direct"],
        datasets:[{
          label:"",
          backgroundColor:["#b24c63","#1cc88a"],
          borderColor:["#ffffff","#ffffff"],
          data:[pont, (10 - pont)]
        }]
      },
      options:{
        maintainAspectRatio:false,
        legend:{
          display:false
        },
        title:{}
      }

      });
     

    })

    axios.get("http://127.0.0.1:5000/api/v1/resources/temperatura?idt_usuario=" + localStorage.id)
    .then(function (response) {
      var arrayValor = [];
      var arrayData = [];
      for(var i = 0; i < response.data.length; i++){
        arrayValor.push(response.data[i].vlr_temperatura);
        arrayData.push(moment(response.data[i].dta_temperatura).format("DD/MM/YYYY"));

      }
      console.log(arrayValor)
      var chartTemp = document.getElementById("tempChart").getContext('2d');
      var tempChart = new Chart(chartTemp,{
        type: "line",
          data:{
            labels:arrayData,
            datasets:[{
              label:"Temperatura",
              fill:true,
              data: arrayValor,
              backgroundColor:"rgba(78, 115, 223, 0.05)",
              borderColor:"rgba(78, 115, 223, 1)"
            }]},
            options:{
              maintainAspectRatio:false,
              legend:{display:false},
              title:{},
              scales:{
                xAxes:[{
                  gridLines:{
                    color:"rgb(234, 236, 244)",
                    zeroLineColor:"rgb(234, 236, 244)",
                    drawBorder:false,
                    drawTicks:false,
                    borderDash:["2"],
                    zeroLineBorderDash:["2"],
                    drawOnChartArea:false
                  },
                ticks:{
                  fontColor:"#858796",
                  padding:20
                }}],
              yAxes:[{
                gridLines:{
                  color:"rgb(234, 236, 244)",
                  zeroLineColor:"rgb(234, 236, 244)",
                  drawBorder:false,
                  drawTicks:false,
                  borderDash:["2"],
                  zeroLineBorderDash:["2"]
                },
                ticks:{
                  fontColor:"#858796",
                  padding:20
                }}]}}}
        
          );
    })

};


function logOff(){
  localStorage.id = null;
}
//Função para bloquear a entrada de não usuários.
if (sessionStorage.getItem('AuthenticationState') === null) {
  window.open("AccessDenied.html", "_self");
}
else if (Date.now > new Date(sessionStorage.getItem('AuthenticationExpires'))) {
     window.open("AccessDenied.html", "_self");
}
else {}