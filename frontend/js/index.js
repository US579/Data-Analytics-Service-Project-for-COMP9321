var submit = document.getElementById("button");


submit.onclick = function(){

    var  username =document.getElementById('username').value
    var  password =document.getElementById('password').value
    if (! username || !password){
        alert('Username and Password can not be empty');
        return
    }
    var url="http://127.0.0.1:5000/login"
    $.ajax({
        url: url,
        type: 'GET',
        data:{
            'username':username,
            'password':password,
        },
        dataType: 'JSONP',
        crossDomain:true,

        success: function(XMLHttpRequest, textStatus,data,xhr){
            var obj = JSON.parse(data.responseJSON);
            if (obj.message == 'authorization has been refused for those credentials.')
            {
                alert('Username and Password are not correct');
                return
            }
            else{
                window.location.href = './main.html';
            }

            //alert('success');
            console.log(data.responseJSON);
            //window.location.href = './main.html';
            
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
            alert("Connection refused")
            
            //alert(XMLHttpRequest.status);
            //alert(XMLHttpRequest.readyState);
            //alert(textStatus);
        }
        
    })
    
  
}

