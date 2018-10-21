var range = document.getElementById("range");
var range_value = document.getElementById("range-value");
var category = document.getElementById("category");
var size = document.getElementById("size");
var price = document.getElementById("price");
var a_ver = document.getElementById("a-ver");
var content_rating = document.getElementById("content-rating");
var reviews = document.getElementById("reviews");
var logout = document.getElementById("logout");
var submit = document.getElementById("submit");
var reset = document.getElementById("reset");
var word_1 = document.getElementById("word-1");
var word_2 = document.getElementById("word-2");
var word_result = document.getElementById("word-result");
var input_div = document.getElementById("input-div");
var result_div = document.getElementById("result-div")
var again = document.getElementById("again")
var name1 = document.getElementById("name1")
var name2 = document.getElementById("name2")

result_div.style.display = "none"
input_div.style.display = "block";

function keySumbit() {
    if (event.keyCode === 13) {
        document.getElementById("submit").click();
        return true
    }
}


again.onclick = function () {
    result_div.style.display = "none"
    input_div.style.display = "block";
    word_1.innerHTML = "Please choose the features";
    word_2.innerHTML = "of your application";
    size.value = '';
    price.value = '';
    reviews.value = '';
    range.value = '5';
    range_value.innerHTML = '5'
    category.value = '1';
    a_ver.value = '0';
    content_rating.value = '1';
    word_1.innerHTML = "Please choose the features";
    word_2.innerHTML = "of your application";
}


function is_number(e) {
    var char_code = e.charCode ? e.charCode : e.keyCode;
    if ((char_code >= 48 && char_code <= 57) || (char_code == 46)) {
        return true;
    }
    else {
        return false;
    }
}

range.onmousemove = function () {
    range_value.innerHTML = range.value;
}

reset.onclick = function () {
    size.value = '';
    price.value = '';
    reviews.value = '';
    range.value = '5';
    range_value.innerHTML = '5'
    category.value = '1';
    a_ver.value = '0';
    content_rating.value = '1';
    word_1.innerHTML = "Please choose the features";
    word_2.innerHTML = "of your application";
}

logout.onclick = function () {
    window.sessionStorage.setItem("token", "");
    window.location.href = './index.html';
}

submit.onclick = function () {
    var reviews = document.getElementById("reviews").value;
    var category = document.getElementById("category").value;
    var content_rating = document.getElementById("content-rating").value;
    var size = document.getElementById("size").value;
    var price = document.getElementById("price").value;
    var a_ver = document.getElementById("a-ver").value;
    var range = document.getElementById("range");
    var range_value = document.getElementById("range-value").innerHTML;

    if (!document.getElementById("reviews").value || !document.getElementById("size").value || !document.getElementById("price").value) {
        alert("Input can not be NULL!");
        return false;
    } else {

        var url = "http://127.0.0.1:5000/predict";

        $(document).ajaxSend(function (event, xhr) {
            if (window.sessionStorage.getItem('token')) {
                xhr.setRequestHeader("AUTH-TOKEN", window.sessionStorage.getItem('token').replace("\"", "").replace("\"", ""));  // 增加一个自定义请求头
            }
        });
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'JSON',
            crossDomain: true,
            data: {
                'reviews': reviews,
                'category': category,
                'rating_of_comparable_app': range_value,
                'size': size,
                'price': price,
                'content_rating': content_rating,
                'Android_version': a_ver,
            },
            success: function (XMLHttpRequest, textStatus, data, xhr) {
                console.log(data)
                var token_str = JSON.stringify(data['responseJSON'].result.replace("\[", "").replace("\]", "").replace("\'", "").replace("\'", ""))
                result_div.style.display = "block"
                input_div.style.display = "none";
                word_1.innerHTML = "The predicted installs number is ";
                word_2.innerHTML = token_str
                name1.innerHTML = (data['responseJSON'].relative_app.split(" "))[0];
                name2.innerHTML = (data['responseJSON'].relative_app.split(" "))[1];
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert('login expire,please login');
            }
        })
    }
}