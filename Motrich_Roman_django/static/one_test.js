//alert('Привет!!!')
console.log('Здорова!!!')



$(document).ready(function(){
    console.log('Page is loaded')

    $('#ajaxButton').on('click',function(e){
        alert('Хватит меня нажимать!!!');
    });

    $('#ajaxButton').on('click',function(e){
        $.get("/ajax_test",function(data){
        $("#testTable1").html(data);
        alert('Load was performed');
        })
    })


})