$(document).ready(function() {
    $('#user').on('submit', function(event) {
        $.ajax({
            method: 'POST',
            url: '/api/v1/insert/usuarios',
            dataType: 'json',
            data : JSON.stringify({
                name : $('#nme_usuario').val(),
                email : $('#eml_usuario').val(),
                password : $('#psw_usuario').val()
            }),
            sucess: function(data) {
                console.log(data);
            }
        })
        .done(function(data) {
            if(data.error) {
                $('#errorAlert').text(data.error).show();
                $('#sucessAlert').hide();
            } else {
                $('#sucessAlert').text(data.name).show();
                $('#errorAlert').hide();
            }
        });

        event.preventDefault();
    });

});