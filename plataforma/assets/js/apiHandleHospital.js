function getCities (){

    const select = document.getElementById('cod_cidade');
  
    axios.get('http://127.0.0.1:5000/api/v1/cidade/all').then(response => {
      this.infos = response.data;
      for(var i = 0; i < infos.length; i++){
        
        var opt = document.createElement('option');
  
        array = Object.entries(infos[i]);
        cidade = array[2].join();
        valor = array[1].join();
        
        opt.value += valor.replace(/idt_cidade,/, '');
        opt.innerHTML += cidade.replace(/nme_cidade,/, '');
        select.appendChild(opt);
      }
      
    });
  };