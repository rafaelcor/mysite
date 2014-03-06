$(document).ready(function(){
    //console.log('opend');
    //$('.send_email').animate({ "left": "-=500px" }, "slow" );
    $('#submit').click(function(){
       try{
           var mail = {'name':    $('.send_email #name_in').val(),
                       'e-mail':  $('.send_email #email_in').val(),
                       'subject': $('.send_email #sub_in').val(),
                       'message': $('.send_email #message').val(),
                       'csrfmiddlewaretoken': $.cookie('csrftoken')};
           $.post('http://localhost/contact/sendmail', mail, function(response) {// //sendmail/ == /contact/sendmail/
               alert(response);
               if(response == 'Yes'){
                   $('.send_email').animate({ "left": "-=500px" }, "slow" );
               }
               else{

               }
           }, 'json');
       }
       catch(err){
           console.log(err);
       }
       $('.send_email').animate({ "left": "-=500px" }, "slow" );

    });

});