window.onload = function() {
    // トーク画面の高さを調整
    var windowHight = $(window).height();
    var headerHight = $("#header").height();
    var footerHeight = $("#footer").height();
    var mainHeight = windowHight - headerHight - footerHeight;
    $("#main-content").css("height", mainHeight + "px")
    // 一番最後までスクロール
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