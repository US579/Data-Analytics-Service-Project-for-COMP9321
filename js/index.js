var submit = document.getElementById("button");

submit.onclick = function () {
    //var  username =document.getElementById('username').value
    //var  password =document.getElementById('password').value
    var url = "http://127.0.0.1:5000/login"
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            'username': 'admin',
            'password': 'admin',
        },
        dataType: 'JSON',
        crossDomain: true,
        success: function (XMLHttpRequest, textStatus, data, xhr) {
            console.log(data)
            var token_str = JSON.stringify(data['responseJSON'].token)
            console.log(typeof (token_str), token_str);
            window.localStorage.setItem('token', token_str);
            window.location.href = './main.htm';
        }
    })
}

