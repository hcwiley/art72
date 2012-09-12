jQuery.event.add(window, 'load', initPieceGallery);
jQuery.event.add(window, 'resize', fitBig);

var showTime = 250;
var imgs = $('imgs');
var curImg = 0;
var lastHeight = $(document).height();
var lastWidth = $(document).width();
var showTime = 450;
var fitDelay = 550;


function initThumbnails(){
    $('#piece').stop().animate({
        opacity: 1
    }, 200);
    img = $('div.other-images > img');
    for (var i = 0; i < $(img).length; i++) {
		$(img[i]).unbind();
        $(img[i]).bind('click', function(){
            time = 450;
            cur = this;
            $('#current-image').animate({
                opacity: 0
            }, time);
            $(this).animate({
                opacity: 0
            }, time);
            window.setTimeout(function(){
                last = $('#current-image').children('img').attr('full');
                //console.log('last: ' + last);
                var newURL = $(cur).attr('full');
//				console.log(newURL);
                $.get(''+newURL, function(){
                    $('#current-image').children('img').attr('src', newURL);
					$('#current-image').children('img').attr('full', newURL);
//                    console.log('now: ' + $(cur).attr('alt'));
                    $(cur).attr('src', last);
					$(cur).attr('full', last);
                    $('#current-image').animate({
                        opacity: 1,
                    }, time);
                    $('#current-image').children('img').animate({
                        opacity: 1,
                    }, time);
                    $(cur).animate({
                        opacity: 1
                    }, time);
                });
            }, time);
			initThumbnails();
//            $('html, body').animate({
//                scrollTop: $('#current-image').offset().top - 30
//            }, 100);
        });
    }
}

function fitBig(){
    justSize();
}

function justSize(){
    //    $("#container").css("left", $(window).width()/2 - 510);
    $('#big-img').width($(window).width());
    $('#big-img').height($(window).height());
    var wide = $('#big-img > img.big-img').width() > $(window).width() - 100;
    var tall = $('#big-img > img.big-img').height() > $(window).height() - 100;
    if (wide || tall) {
        if (wide) {
            $('#big-img > img.big-img').width($(window).width() - 200);
            $('#big-img > img.big-img').height('auto');
        }
        else if (tall) {
            $('#big-img > img.big-img').height($(window).height() - 50);
            $('#big-img > img.big-img').width('auto');
        }
    }
    else {
        $('#big-img > img.big-img').width($(window).width() - 100);
        $('#big-img > img.big-img').height('auto');
    }
    $('#big-img > div:not(#close-big)').height($(window).height());
    $('#big-img > div:not(#close-big) > img').css('top', ($(window).height() / 2));
    $('#big-img > img.big-img').css('top', ($(window).height() - $('#big-img > img.big-img').height()) / 2);
    $('#big-img > img.big-img').css('left', ($(window).width() - $('#big-img > img.big-img').width()) / 2);
}

function closeBig(){
    $('#big-img').animate({
        opacity: 0,
        width: 0,
        height: 0,
        left: '+=' + $(window).width() / 2,
        top: '+=' + $(window).height() / 2
    }, showTime);
    $('#big-img').css('z-index', '-1');
    $('body').css('overflow','auto');
}

function changeImage(dir){
    if (dir < 0) {
        //console.log('left');
        if (curImg == 0) 
            curImg = imgs.length - 1;
        else 
            curImg--;
    }
    else if (dir > 0) {
        //console.log('right');
        if (curImg == imgs.length - 1) 
            curImg = 0;
        else 
            curImg++;
    }
    $('#big-img > img.big-img').stop(true, true).animate({
        opacity: 0
    }, showTime);
    window.setTimeout(function(){
        var newSrc = $(imgs[curImg]).attr('src');
        if (newSrc.match('thumb')) {
            newSrc = newSrc.replace('thumbs/', '');
        }
        $.get(newSrc, function(){
            $('#big-img > img.big-img').attr('src', newSrc);
            window.setTimeout(function(){
	            fitBig();
                $('#big-img > img.big-img').stop(true, true).animate({
                    opacity: 1
                }, showTime);
            }, fitDelay + 20);
        });
    }, showTime + 20);
}

function initMainImage(){
    imgs = $('img:not(.ignore)');
    $('#current-image').bind('click', function(){
        var newSrc = $('#current-image').children('img').attr('full');
		console.log(newSrc);
        for (var i = 0; i < $(imgs).length; i++) {
            if ($(imgs[i]).attr('full') == $('#current-image > img.big-img').attr('full')) {
                curImg = i;
                break;
            }
        }
        $('#big-img > img.big-img').attr('src', newSrc);
		$('body').css('overflow','hidden');
        window.setTimeout("fitBig();", fitDelay);
        $('#big-img').css('z-index', '10');
        $('#big-img').css('top', $(window).height() / 2);
        $('#big-img').css('left', $(window).width() / 2);
        window.setTimeout(function(){
            $('#big-img').animate({
                opacity: 1,
                left: '-=' + $(window).width() / 2,
                top: '-=' + $(window).height() / 2,
                width: $(window).width(),
                height: $(window).height()
            }, showTime);
        }, 20);
        //        $('#big-img').show();
    });
    $('#big-img > img.big-img').bind('click', function(){
        closeBig();
    });
    $('#prev').bind('click', function(){
        changeImage(-1);
    });
    $('#next').bind('click', function(){
        changeImage(1);
    });
    $('#close-big').add('#close-big').bind('click', function(){
        closeBig();
    });
    $(document).bind('keydown', function(event){
        if (event.keyCode == 27 || event.which == 27) {
            closeBig();
        }
        else if (event.keyCode == 37 || event.which == 37) {
            changeImage(-1);
        }
        else if (event.keyCode == 39 || event.which == 39) {
            changeImage(1);
        }
    });
}


function initPieceGallery(){
    initThumbnails();
	window.setTimeout(function(){
        initMainImage();
	}, 500);
    window.setTimeout(function(){
        imgs = $('img').not('.ignore');
        $('img').mousedown(function(event){
            if (event.which == 3) {
                $('body').hide();
                window.setTimeout("$('body').show();", 2);
            }
        });
    }, 300);
	$('iframe').unbind();
	full = $('[full]');
	for (var i = 0; i < $(full).length; i++){
		var img = $(full[i]);
		var src = $(full[i]).attr('full');
		window.setTimeout(function(){ 
		$.get(src, function(data){
			console.log('got my image');
		});
		}, 1000);
	}
}
