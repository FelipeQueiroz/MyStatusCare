function getHospital (){

    const table = document.getElementById('dataTable');
  
    axios.get('http://127.0.0.1:5000/api/v1/hospital/all').then(response => {
      this.infos = response.data;
      for(var i = 0; i < infos.length; i++){
        
        var opt = document.createElement('option');
  
        array = Object.entries(infos[i]);
        console.log(array)
        
        /*opt.value += valor.replace(/idt_cidade,/, '');
        opt.innerHTML += cidade.replace(/nme_cidade,/, '');
        select.appendChild(opt);*/
      }
      
    });
  };