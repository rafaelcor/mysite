$(document).ready(function(){
    var submit = $('#login_button');

    var user = $('#user_entry');
    var pass = $('#password_entry');
    $('#labelc').css('visibility', 'hidden');
    submit.click(function(){
        try{
        user_val = user.val();
        pass_val = pass.val();
         var obj = {'user': user_val,
                    'password': pass_val,
                    'csrfmiddlewaretoken': $.cookie('csrftoken')};

         $.post('/login_request/', obj, function(data) {
             console.log(data);
             if (data['login'] == "wrong"){
                 console.log(data);//despues hay que agregar label de error
                 $('#labelc').css('visibility', 'visible');
             }
             else{
                 $(location).attr('href','entries/');
             }

             });}
          catch(err){
              $('#labelc').val('Debe ingresar un usuario y una contraseña');
              $('#labelc').css('visibility', 'visible');
          }

    });
    pass.keyup(function(e){
                try{
                if (e.keyCode == 13)//13 es el keycode de enter
                 {
                    user_val = user.val();
                    pass_val = pass.val();
                     var obj = {'user': user_val,
                                'password': pass_val,
                                'csrfmiddlewaretoken': $.cookie('csrftoken')};

                     $.post('/login_request/', obj, function(data) {
                         console.log(data);
                         if (data['login'] == "wrong"){
                             console.log(data);//despues hay que agregar label de error
                             $('#labelc').css('visibility', 'visible');
                         }
                         else{
                             $(location).attr('href','entries/');
                         }

                         });


                 }}
                 catch(err){
                     $('#labelc').val('Debe ingresar un usuario y una contraseña');
                     $('#labelc').css('visibility', 'visible');
                 }

            });
});