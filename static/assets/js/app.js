const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");
hamburger.addEventListener('click', ()=>{
   //Animate Links
    navLinks.classList.toggle("open");
    links.forEach(link => {
        link.classList.toggle("fade");
    });

    //Hamburger Animation
    hamburger.classList.toggle("toggle");
});
// popum login-------------------------------------

function change_text(){
    return(document.getElementById("singlepdct_size").innerHTML = "M");
}
function functionl(){
  return(document.getElementById("singlepdct_size").innerHTML="L");
}
function functions(){
  return(document.getElementById("singlepdct_size").innerHTML="S")
}
function functionxl(){
  return(document.getElementById("singlepdct_size").innerHTML="XL")
}
function functionxxl(){
  return(document.getElementById("singlepdct_size").innerHTML="XXL")
}
// Quantity updating function for single product 
function increaseValue_single_pdct() {

    var value = parseInt(document.getElementById('sing_product_quantity').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('sing_product_quantity').value = value;
  }

  function decreaseValue_single_pdct() {
    var value = parseInt(document.getElementById('sing_product_quantity').value, 10);
    value = isNaN(value) ? 0 : value;
    value < 1 ? value = 1 : '';
    value--;
    document.getElementById('sing_product_quantity').value = value;
  }
  

  function myRedFunction() {
    document.getElementById("heart").style.color = "red";
  }
  

  // password secret

  $(function () {
    var Accordion = function (el, multiple) {
      this.el = el || {};
      this.multiple = multiple || false;

      // Variables privadas
      var links = this.el.find('.link')[0];
      // Evento
      links.on('click', { el: this.el, multiple: this.multiple }, this.dropdown)
    }

    Accordion.prototype.dropdown = function (e) {
      var $el = e.data.el;
      $this = $(this),
      $next = $this.next();

      $next.slideToggle();
      $this.parent().toggleClass('open');

      if (!e.data.multiple) {
        $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
      };
    }

    var accordion = new Accordion($('#accordion'), false);
  });
// heart---------------------------
    $(".js-fav").on("click", function() {
        $(this).find('.heart').toggleClass("is-active");
    });

    function openNav(){
      document.getElementById("mySidenav").style.width="250px";
      var cart_cookie = getCookie("cart_product")
      if (cart_cookie != null){
        var cart_product_list = JSON.parse(cart_cookie)
          $('#cart_append').empty()
        for (let i = 0; i < cart_product_list.length; i++) {
                var appending_div = $('<div class="billing-product-1 d-flex" id="cartcount'+i+'"><div class="prdt-img-1"><img src="'
                                      +cart_product_list[i].singlepdct_image
                                      +'" alt=""></div><div clas="prdt-text-1"><p>'
                                      +cart_product_list[i].product_name
                                      +'</p><p class="prdt_price">₹<span class=side_cart_price>'
                                      +cart_product_list[i].product_price
                                      +'</span></p></div><div class="prdt-icon-1" onclick="remove_from_cart('+i+')"><i class="fas fa-times"></i></div></div>'
                )
                  $('#cart_append').append(appending_div)
        }
      }
      update_cart_total()
    }
    function closeNav(){
      document.getElementById("mySidenav").style.width="0";
    }


    function remove_from_cart(id,token){
      
      var cart_cookie = getCookie("cart_product")

      if (cart_cookie != null){
        var cart_list = JSON.parse(cart_cookie)
        if (document.token){
          /**
           * 
           */

          var response_status =  ajax_call_remove_cart(cart_list[id].product_name,cart_list[id].product_id)
        
          if (response_status){
        
        
            cart_list.splice(id,1);
  
            setCookie('cart_product',JSON.stringify(cart_list),3)
          }
          
        }
        else{
          cart_list.splice(id,1);
  
          setCookie('cart_product',JSON.stringify(cart_list),3)
        }
        openNav()
      }

    }

    function add_to_cart(id,name,price,image,quantity,size){
      console.log("<<<<<<<<<<<<",name)

      var product_id = id
      var product_name = name
      var product_price = price
      var product_quantity = quantity
      var singlepdct_image = image
      var product_size =size
      var cart_cookie = getCookie("cart_product")
      if (cart_cookie != null && cart_cookie.length >= 0 ){
        // cart_list.push(JSON.parse(cart_cookie))
        var cart_list = JSON.parse(cart_cookie)
        var temp_list = {
          "product_id":product_id,
          "product_name":product_name,
          "product_price":product_price,
          "product_quantity":product_quantity,
          "singlepdct_image":singlepdct_image,
          "product_size":product_size
        }

        if (cart_list.length < 0){
          for(var i = 0; i < cart_list.length; i++){
            if (cart_list[i].product_id == product_id){              
              cart_list[i].product_quantity = parseInt(cart_list[i].product_quantity) + 1
            }
            else{
              cart_list.push(temp_list)
            }
          }
        }else{
          cart_list.push(temp_list)
        }
        
        setCookie('cart_product',JSON.stringify(cart_list),3)
        success_alert("product add to cart")
      }
      else{
        
        var temp_list = {
          "product_id":product_id,
          "product_name":product_name,
          "product_price":product_price,
          "product_quantity":product_quantity,
          "singlepdct_image":singlepdct_image,
          "product_size":product_size,
        }

        var list =  []
        list.push(temp_list)
        setCookie('cart_product',JSON.stringify(list),3)
        success_alert("product add to cart")

      }
        var e = $('<div style="display:block; float:left;width:'+width+'px; height:'+height+'px; margin-top:'+positionY+'px;margin-left:'+positionX+'px;border:1px dashed #CCCCCC;"></div>');
        $('#cart_append').append(e);
        
    }

    function setCookie(name, value, daysToLive) {
        let date = new Date();
        date.setTime(date.getTime() + (daysToLive * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = name + "=" + value + "; " + expires + "; path=/";
    }

    function getCookie(name) {

      var cookieArr = document.cookie.split(";");

      for(var i = 0; i < cookieArr.length; i++) {
          var cookiePair = cookieArr[i].split("=");

           if(name == cookiePair[0].trim()) {
              // Decode the cookie value and return
              return decodeURIComponent(cookiePair[1]);
          }
      }
      return null;
    }


  function ajax_call_remove_cart(name,id){
    var bool = 0
    return $.ajax({
      url: '/api/delete_user_cartlist/', // url where to submit the request   
      type : 'GET', // type of action POST || GET
      data : {
            'product_name':name,
            'product_id': id
        },
      beforeSend: function (xhr) {
          xhr.setRequestHeader('Authorization', 'Token '+document.token);
      },
      success : function(messgae) {
          // you can see the result from the console
          // tab of the developer tools
          true
      
      },
      error: function(xhr, resp, text) {
          // alert here if want to show the user response
          false
          
      }
    })
    
  }
  function heart_wishlist(e,name,id) {
      var product_name = name
      var product_id = id

      if($(e).find('.heart').hasClass("is-active")){
          $.ajax({
            url: '/api/delete_user_wishlist/', // url where to submit the request   
            type : 'GET', // type of action POST || GET
            data : {
                 'product_name': product_name,
                 'product_id': product_id
             },
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', 'Token '+document.token);
            }, 
            success : function(messgae) {
                // you can see the result from the console
                // tab of the developer tools
                $(e).find('.heart').removeClass("is-active");
                success_alert('product remove to wishlist')
            },
            error: function(xhr, resp, text) {
                // alert here if want to show the user response
            }
          })
        }
      else{
          $.ajax({
            url: '/api/add_user_wishlist/', // url where to submit the request   
            type : 'GET', // type of action POST || GET
            data : {
                 'product_name': product_name,
                 'product_id': product_id,
             },
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', 'Token '+document.token);
            },
            success : function(messgae) {
                // you can see the result from the console
                // tab of the developer tools
                $(e).find('.heart').addClass("is-active");
                success_alert('product add to wishlist')
            },
            error: function(xhr, resp, text) {
                // alert here if want to show the user response
            }
          })
        }
  }

  function cart_wish_list(e,name ,id,image,quantity,token,price,size){
    var product_name = name
    var product_id = id
    var product_quantity = quantity
    var product_size = size
    $.ajax({
      url: '/api/add_user_cartlist/', // url where to submit the request   
      type : 'GET', // type of action POST || GET
      data : {
            'product_name': product_name,
            'product_id': product_id,
            'product_quantity': product_quantity,
            'product_size': product_size,
        },
      beforeSend: function (xhr) {
          xhr.setRequestHeader('Authorization', 'Token '+token);
      },
      success : function(response) {
          // you can see the result from the console
          // tab of the developer tools
          add_to_cart(id,name,price ,image,quantity,size)
      },
      error: function(xhr, resp, text) {
          // alert here if want to show the user response
      }
    })
  }


  function update_cart_table(){
    var cart_cookie = getCookie("cart_product")
    if (cart_cookie != null){
      var cart_product_list = JSON.parse(cart_cookie)
      $('#cart_append_card').empty()
      for (let i = 0; i < cart_product_list.length; i++) {
              var appending_div = $('<div class="row border-cart ">'+
                                    '<div class="col-md-4  col-lg-4 col-sm-6 col-xs-6  img-text-cart">'+
                                    '<div class="small-jkt-img d-flex">'+
                                        '<a href="singlepdct.html"><img src="'+
                                        cart_product_list[i].singlepdct_image+
                                        '"></a>'+
                                        '<h4>'+cart_product_list[i].product_name+'</h4> '+
                                    '</div>'+
                                '</div>'+
                                '<div class="col-md-4 col-lg-4 col-xs-6 col-sm-6 dropdown-cart d-flex">'+
                                        
                                '<p class="span-cart-552" >Size : <span>'+ cart_product_list[i].product_size+'</span></p>'+
                                '</div>'+
                                '<div class="col-md-2 col-lg-2 col-sm-6 col-xs-6 d-flex cart-qty">'+
                                '<div class="plus-minus-button">'+
                                '<form class="d-flex text-center">'+

                                '<input type="number" id="number" class="number singlepdct_qunatity" disabled value='+ cart_product_list[i].product_price+' />'+
                                '</form>'+
                                '</div>'+
                                '</div>'+
                                '<div class="col-md-2 col-lg-2 col-sm-6 col-xs-6 cart-price">'+
                                '<div class="main-552 text-center">'+
                                '<p class="span-cart-552" >₹<span class="cart_price">'+cart_product_list[i].product_price+'</span></p>'+
                                            '</div>'+
                                        '</div>'+
                                        '<span><i class="fas fa-times cross-wrong"></i></span>'+
                                '</div>')
                $('#cart_append_card').append(appending_div)
      }
    } 
  }


  function clear_cart(){
    setCookie('cart_product',JSON.stringify([]),3)
  }


  function update_cart_total (){
      var total_price = 0
      for(var i = 0; i < document.getElementsByClassName('side_cart_price').length; i++){
          var price = parseInt(document.getElementsByClassName('side_cart_price')[i].innerHTML)
          total_price = total_price + price
      }
      document.getElementById('side_cart_total').innerHTML = total_price
  }
  
  function update_checkout_total(){
      var total_price = 0
      for(var i = 0; i < document.getElementsByClassName('checkout_cart_price').length; i++){
          var price = parseInt(document.getElementsByClassName('checkout_cart_price')[i].innerHTML)
          total_price = total_price + price
      }
      
      document.getElementById('checkout_price').innerHTML = total_price
      document.getElementById('checkout_shipping').innerHTML = 2
      document.getElementById('total_checkout_price').innerHTML = parseInt(total_price) + parseInt(document.getElementById('cart_shipping').innerHTML)
  }


  /**
   * Rating star product start
   */
  
   
  
  /**
   * Rating star product end
   */



  