const toggleLoader = ()=>{
    document.getElementById('loader').classList.toggle("d-none")
 
        
}

const requestBlood = (id) => {
    toggleLoader();
    const donorid = id;
    // console.log(donorid);
    $.ajax({
        type: "POST",
        url: "/requestblood ",
        data: {
            'id':donorid,
        },
        success: function(response) {
            if(response.success === true){
                toggleLoader();
                new swal("Message Sent", "", "success")
                
                // swal({
                //     title:"Message Sent",
                   
                //     icon: "success"
                //   });
            }
            
        },
        failure: function(response) {
            
            // console.log(response);
            toggleLoader();
        },
        error: function(error) {
            // console.log(error);
            toggleLoader();
            new swal("Something Went wrong", "", "error")
                
        }



    })
   
}