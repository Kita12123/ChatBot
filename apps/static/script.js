window.onload = function() {
    // 一番最後までスクロール
    console.log("スクロールfunction実行")
    var container = document.getElementById("main-content");
    container.scrollTop = container.scrollHeight
}

function Loading(){
    var inMes = document.getElementById("message").value;
    document.getElementById("inMessage").textContent = inMes
    document.getElementById("loading").style.display = '';
    var container = document.getElementById("main-content");
    container.scrollTop = container.scrollHeight
}