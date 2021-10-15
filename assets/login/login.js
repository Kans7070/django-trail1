// $('.error-page').hide(0);

// $('.login-button , .no-access').click(function(){
//   $('.login').slideUp(500);
//   $('.error-page').slideDown(1000);
// });

// $('.try-again').click(function(){
//   $('.error-page').hide(0);
//   $('.login').slideDown(1000);
// });
$("#login").validate({
  rules:{
      username:{
          required:true, 
      },
            
      password:{
          required:true,
      }
  
  }
  })