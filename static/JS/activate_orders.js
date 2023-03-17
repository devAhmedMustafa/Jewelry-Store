let orders = document.querySelectorAll('.status')

orders.forEach(function(order){

    let orderStatus = order.firstElementChild.value;
    let orderId = order.lastElementChild.value;
    let button = order.childNodes[3];
    console.log(orderStatus);

    order.addEventListener('click', function(){
        $.ajax({

            url: '/ajax/order_status/',
            data: {'order_id': orderId, 'status': orderStatus},
            dataType: 'json',
            success: function(data){
                if ( data.status == 'delivered' ){
                  button.innerHTML = 'Delivered';
                  button.style.animation = 'coloringGreen 1s';
                  button.style.backgroundColor = 'green';
                }
                else if ( data.status == 'on_your_way'){
                  button.innerHTML = 'Out for delivery';
                  button.style.animation = 'coloringGrey 1s';
                  button.style.backgroundColor = 'grey';
                }
            }
    
        })
    })
});