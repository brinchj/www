var html_404 = "not found.\
<script type='text/javascript'>                 \
  var GOOG_FIXURL_LANG = 'en';\
  var GOOG_FIXURL_SITE = 'http://diku.dk/hjemmesider/studerende/zerrez/';\
</script>\
<script type='text/javascript'\
    src='http://linkhelp.clients.google.com/tbproxy/lh/wm/fixurl.js'></script>";

function recvContext(req) {    
    if (req.status == 200) {
        document.getElementById("right").innerHTML = req.responseText;
    } else if (req.status == 404) {
        document.getElementById("right").innerHTML = html_404;
    }
}

function loadContext() {
    path = location.href;
    if (path.indexOf("?") < 0) {
        path = '?personal/contact';
    }

    document.getElementById("right").innerHTML="loading..";
    path = path.substring(path.indexOf("?")+1);

    url = "sections/" + path + ".html";
    var req = new XMLHttpRequest();
    req.open("GET", url, true);
    req.onreadystatechange = function() {recvContext(req)};
    req.send(null);
}