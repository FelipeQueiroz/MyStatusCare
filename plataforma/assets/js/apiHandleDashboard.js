document.getElementsByTagName('body').addEventListener("load", onLoad);

function onLoad(e){
    axios.get("http://127.0.0.1:5000/api/v1/usuarios/all")
    .then(response => {
        this.infos = response.data;
        console.log(this.infos);
      })

    e.preventDefault();

}