function recvContext(req) {    
    if (req.status == 200) {
        document.getElementById("right").innerHTML = req.responseText;
    } else if (req.status == 404) {
        document.getElementById("right").innerHTML = "not found.";
    }
}

function loadContext() {
    path = location.href;
    if (path.indexOf("?") > 0) {
        document.getElementById("right").innerHTML="loading..";
        path = path.substring(path.indexOf("?")+1);
        url = "sections/" + path + ".html?" + Math.random();
        var req = new XMLHttpRequest();
        req.open("GET", url, true);
        req.onreadystatechange = function() {recvContext(req)};
        req.send(null);
    }
}