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


function keySumbit(){
    
    if (event.keyCode === 13) {
        document.getElementById("submit").click(); 
    return true
 }
}




function is_number(e){
    var char_code = e.charCode ? e.charCode : e.keyCode;
    if((char_code>=48 && char_code <= 57) || ( char_code == 46)){
        return true;
    }
    else{
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
    content_rating.value = '0';
    word_1.innerHTML = "Please choose the features";
    word_2.innerHTML = "of your application";
}

logout.onclick = function () {

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
    var range_value = document.getElementById("range-value").value;
    alert(range_value)
    console.log(range_value)
    //alert(category)
    //alert(range_value)
    //alert(reviews)
    //alert(size)
    //alert(price)
    //alert(content_rating)
    //alert(a_ver)
    if(!document.getElementById("reviews").value || !document.getElementById("size").value || !document.getElementById("price").value)
    {
        alert("Input can not be NULL!");
        return false;
    }else{

    //word_1.innerHTML = "The predicted installs are:";
    //word_2.innerHTML = "0";
    //request.setRequestHeader("AUTH-TOKEN", window.localStorage.getItem('token')
    //alert(window.localStorage.getItem('token'))
    var url = "http://127.0.0.1:5000/predict";
    //var xhr = new XMLHttpRequest();
    //xhr.open('GET', url, true);
    //xhr.setRequestHeader('AUTH-TOKEN', window.localStorage.getItem('token'))
    $(document).ajaxSend(function (event, xhr) {
            xhr.setRequestHeader("AUTH-TOKEN",window.localStorage.getItem('token').replace("\"","").replace("\"","") ) ;  // 增加一个自定义请求头
    });
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'JSON',
        crossDomain: true,
        //xhr.setRequestHeader('AUTH-TOKEN', window.localStorage.getItem('token')),
        //beforeSend: function (request) {
          //  request.setRequestHeader("AUTH-TOKEN", window.localStorage.getItem('token'));
        //},
        data: {
            'reviews': reviews,
            'category': category,
            'rating_of_comparable_app':4,
            'size': size,
            'price': price,
            'content_rating': content_rating,
            'Android_version': a_ver,
        },

        success: function (XMLHttpRequest, textStatus, data, xhr) {
            console.log(data)
            var token_str = JSON.stringify(data['responseJSON'].result.replace("\[","").replace("\]","").replace("\'","").replace("\'","") )
            //alert(token_str)
             word_1.innerHTML = "the predict installs number is ";

             word_2.innerHTML = token_str;
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
             alert('login expire,please login');
            //alert(XMLHttpRequest.status);
            //alert(XMLHttpRequest.readyState);
            //alert(textStatus);
        }
    })
}}