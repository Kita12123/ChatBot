window.onload = function() {
    // 一番最後までスクロール
    console.log("スクロールfunction実行")
    var container = document.getElementById("main-content");
    container.scrollIntoView(false);
}

function Loading(){
    var inMes = document.getElementById("message").value;
    // 入力文字が表示できん
    //document.getElementById("inMessage").innerHTML(inMes);
    document.getElementById("loading").style.display = '';
    var container = document.getElementById("main-content");
    container.scrollIntoView(false);
}