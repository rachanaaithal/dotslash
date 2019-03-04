window.onload=function(){

    function disp(d){
        var out= $('<div/>')
        var div= $('<div/>');
        div.addClass('card');    
        div.append(`<img src=${d.url} class="hotel_img card-img-top">`);
        var cardbody= $('<div/>');
        cardbody.attr('id',`${d.id}`);
        cardbody.addClass('card-body');
        cardbody.append(`<h5 class='card-title'>${d.question}</h5>`);
        cardbody.append(`<div class="form-group"><label for="comment">Answer:</label><textarea class="form-control" rows="5" id="comment"></textarea></div>`)
        cardbody.append(`<button type="button" class="btn btn-primary answer" >Submit</button>`)
        
        div.append(cardbody);
        out.append(div);
        out.addClass('col-md-4')
        out.appendTo('#main-body');
    }

    



    $.ajax({
        url: "http://127.0.0.1:5000/requests",
        cache: false,
        success: function(data){
            console.log(data);
            $("#main-body").html('');
            data.map(function(d){
                console.log(d.url);
                disp(d);
            });
            $(".answer").click(function(e){
                //console.log(e.target.parentElement.parentElement);
                //console.log(e.target.parentElement.id);
                answer=e.target.parentElement.firstChild.nextSibling.firstChild.nextSibling.value;
                response={'id':e.target.parentElement.id,'response':answer};
                console.log(response);
                $.ajax({
                    url: "http://127.0.0.1:5000/send_string",
                    contentType: 'application/json;charset=UTF-8',
                    type: 'POST',
                    data: response,
                    success: function(response) {
                        console.log("done");
                    },
                    error: function(error) {
                        console.log("error");
                    }
                });
            });
        }
    });

    
    
}