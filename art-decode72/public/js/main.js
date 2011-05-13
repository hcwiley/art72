jQuery.event.add(window, 'resize', resize);
jQuery.event.add(window, 'load', init);
var img_ratio;
//Current page = loc
var loc;

mobile = false;

//Checking for mobile browser
if (navigator.userAgent.match(/Android/i) ||
navigator.userAgent.match(/webOS/i) ||
navigator.userAgent.match(/iPhone/i) ||
navigator.userAgent.match(/iPod/i)) {
    mobile = true;
}

function init(){
	//Current page = loc
    loc = window.location + "";
    loc = loc.split('/');
    loc = loc[loc.length - 1];
    if (loc[0, 4] == 'index' || loc == '') {
        img_width = $("#bg-img").children("img").width()
        img_height = $("#bg-img").children("img").height();
        img_ratio = img_width / img_height;
    }
    resize();
    imgs = $('img');
    for (var i = 0; i < imgs.length; i++) {
        $(imgs[i]).attr('src', ($(imgs[i]).attr('src') + '').split('.com')[1]);
    }
}

function resize(){
    var height = $(window).height();
    var width = $(window).width();
    bg(width, height);
    $("#container").width(width - 300);
    $("#container").css("left", (width - $("#container").width()) / 2);
    $("#footer").css("top", $("#container").height() + 10);
}

function bg(width, height){
    $("#bg-img").width(width);
    $("#bg-img").height(height);
    $("#bg-img").css("top", "-10px");
    $("#bg-img").css("left", "-10px");
    var img = $("#bg-img").children("img");
    var ratio = height / width;
    img.css("width", width + 20);
    img.css("height", (width / img_ratio) + 20);
}
