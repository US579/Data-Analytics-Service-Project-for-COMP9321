
var submit = document.getElementById("button");
function keyLogin() {

    if (event.keyCode === 13) {
        document.getElementById("button").click();
        return true
    }
}
submit.onclick = function () {
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    if ((!username) || (!password)) {
        alert('username and password can not be empty')
        return
    }
    var url = "http://127.0.0.1:5000/login"
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            'username': username,
            'password': password,
        },
        dataType: 'JSON',
        crossDomain: true,
        success: function (XMLHttpRequest, textStatus, data, xhr) {
            console.log(data)
            var token_str = JSON.stringify(data['responseJSON'].token)
            console.log(typeof (token_str), token_str);
            window.sessionStorage.setItem('token', token_str);
            window.location.href = './main.html';
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert('username and password are not correct.');
            window.location.href = './index.html';
        }
    })
}



