window.onload=function(){

    function disp(d){
        
    }


    $.ajax({
        url: "http://127.0.0.1:5000/requests",
        cache: false,
        success: function(data){
            console.log(data);
            $("#main-body").html('');
            data.map(function(d){
                console.log(d.question);
                disp(d);
            });
        }
    });
}