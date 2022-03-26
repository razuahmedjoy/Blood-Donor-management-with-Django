const ApiKey = "WBJWw8+MaSFdY6OWcLj/9ToSyrcG/wR2A+Ls2y+SgGw="
const ClientId = "5ea4395a-03e4-4494-b647-617b81f290b1"
const SenderId = "8804445649863"
const MobileNumbers = "01787260577"
const Message = "This is a test message by Razu"


const test = ()=> {       
    $.ajax({
        type: "GET",
        url: `http://fsms.fantasyhost.com.bd:6005/api/v2/SendSMS?ApiKey=${ApiKey}&ClientId=${ClientId}&SenderId=${SenderId}&Message=${Message}&MobileNumbers=${MobileNumbers}`,
        contentType: "application/json",
        dataType: 'json',           
        success: function (response) {  
            console.log(response)              
        }
    });
}
test();
