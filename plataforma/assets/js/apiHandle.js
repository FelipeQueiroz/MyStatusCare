$(document).ready(function() {
    $('.formUser').on('submit', function(event) {
        $.ajax({
            data : {
                name : $('#nme_usuario').val(),
                email : $('#eml_usuario').val(),
                password : $('#psw_usuario').val()
            },
            type: 'POST',
            url: '/api/v1/insert/usuarios'
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