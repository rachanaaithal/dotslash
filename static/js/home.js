window.onload=function(){

    $.ajax({
        url: "127.0.0.0:5000/requests/",
        cache: false,
        success: function(data){
            console.log(data);
        }
    });
}