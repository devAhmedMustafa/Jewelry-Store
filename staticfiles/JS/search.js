$('#search').change( function(){
    $.ajax({
        url: '/ajax/search/',
        data: {'searchInput': $(this).val()},
        dataType: 'json',
        success: function(data){
            console.log('done')
        }
    })
} )