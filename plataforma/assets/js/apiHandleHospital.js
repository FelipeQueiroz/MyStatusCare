function getHospital (){

  const table = document.getElementById('tableRow');
  
    axios.get('http://api-msc.educatux.com.br/api/v1/hospital/all').then(function (response){
      for(var i = 0; i < response.data.length; i++){
        
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);

        cell1.innerHTML = response.data[i].nme_hospital;
        cell2.innerHTML = response.data[i].nme_estado;
        cell3.innerHTML = response.data[i].nme_cidade;
        table.appendChild(row);
      }
      
    });
  };

  function searchInput() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("tableRow");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }