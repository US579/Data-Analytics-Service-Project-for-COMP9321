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


range.onmousemove = function(){
    range_value.innerHTML = range.value;
}

reset.onclick = function(){
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

logout.onclick = function(){
    window.location.href = 'index.htm';
}

submit.onclick = function(){
    word_1.innerHTML = "The predicted installs are:";
    word_2.innerHTML = "0";

}