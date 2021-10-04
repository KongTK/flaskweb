/* 사진 바꾸기 */
// 이벤트가 2개 이상인 경우 - addEventListener() 함수 사용
pic = document.getElementById('pic');

//마우스를 올리고 내렸을때 이벤트
pic.addEventListener("mouseover", function(){ //주의 on을 생략
    pic.src = "../static/images/coffee-pink.jpg";
});

pic.addEventListener("mouseout", function(){
    pic.src = "../static/images/coffee-blue.jpg";
});

/* 디지털 시계 */
setInterval(myWatch, 1000)

function myWatch(){
    var date = new Date();
    var now = date.toLocaleTimeString();
    document.getElementById('demo').innerHTML = now;
}
