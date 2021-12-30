$(document).ready(function (){
    console.log("done");    
    $(document).on("submit", "form.ajax", function(e){
        e.preventDefault();
        var $this = $(this);

        var url = $this.attr("action");
        var method = $this.attr("method")

        $.ajax({
            type:method,
            url:url,
            dataType: "json",
            data: new FormData(this),
            processData: false,
            contentType: false,
            cache: false,
            success: function (data){
                console.log("=========success");
                console.log(data);

                var title = data["title"];
                var message = data["message"];
                var status = data["status"];  

                Swal.fire({
                    icon: status,
                    title : title,
                    text : message
                });

                if(status == "error"){
                    $this.trigger("reset")
                }
            },
            error: function(error){
                console.log("==========error");
                console.log(error);
            },

        });

    });
});
