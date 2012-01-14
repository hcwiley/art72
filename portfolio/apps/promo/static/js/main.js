jQuery.event.add(window, 'resize', resize);
jQuery.event.add(window, 'load', init);
jQuery.event.add(window, 'unload', leave);

//Current page = loc
var loc;
var isMobile = false;
var isIE = false;
var fadeDelay = 400;
var changing = false;
var invalidEmail = "";
var required_email = "";
var required_message = "";
var required_name = "";
var goingOut = false;

//Checking for mobile browser
if (navigator.userAgent.match(/Android/i) ||
navigator.userAgent.match(/webOS/i) ||
navigator.userAgent.match(/iPhone/i) ||
navigator.userAgent.match(/iPod/i)) {
    isMobile = true;
}

if (jQuery.browser.msie) {
    isIE = true;
}

function sexyScroll(to, time){
    if (!to) {
        to = 0;
    }
    if (!time) {
        time = 10;
    }
    //	printf($(document).scrollTop());
    var pos = $(document).scrollTop();
    var delta = 200;
    if (pos > to) {
        window.setTimeout(function(){
            if (pos - delta < to) {
                delta = pos - to;
            }
            $(document).scrollTop(pos - delta);
            window.setTimeout("sexyScroll();", time);
        }, time * 2);
    }
}

function animateOut(){
    $('#container').addClass('noborders');
    $('#container').data('left-width', $('div.bottom > div.left').width());
    $('div.bottom > div.left').add($('div.bottom-copy')).animate({
        width: 0,
    }, fadeDelay).hide(0);
    $('#wrapper').data('height', $('#wrapper').height());
    window.setTimeout(function(){
        $('#wrapper').stop().animate({
            top: -2000
        }, fadeDelay * 2);
    }, fadeDelay);
}

function leave(event){
    event.preventDefault();
    window.setTimeout(function(){
        animateOut();
    }, 10);
}

function animateIn(loc){
    sexyScroll();
    window.setTimeout("$('#container').removeClass('noborders');", fadeDelay);
    $('.current-page').removeClass('current-page');
    if (loc == '/') {
        var id = '#home';
    }
    else {
        var id = '#' + loc.replace('/', '');
    }
	$('.cur-page').removeClass('cur-page');
    $('a[href='+loc+']').addClass('cur-page');
    $.ajax({
        url: '/ajax' + loc,
        type: 'get',
        success: function(data){
            var title = $($(data)[0]).text();
            if (!isIE) {
                $('title').text(title);
            }
            var html = '';
            var id = '';
            data = $(data);
            for (var i = 0; i < $(data).length; i++) {
                id = $(data[i]).attr('id');
                if (id == 'content') {
                    html += $(data[i]).html();
                }
            }
            $('#main').html(html);
			$(html).ready(function(){
				resize();
			});
            window.setTimeout(function(){
                $('#wrapper').stop().animate({
                    top: 0, 
                }, fadeDelay);
            }, fadeDelay*2);
            reinit();
            $('div.bottom > div.left').width($('#container').data('left-width'));
        },
        error: function(xhr, statusText, errorThrown){
            var html = xhr.response;
            html = $(html).find('.center');
            $('#main').html(html);
            $('#wrapper').stop().animate({
                top: 0,
            }, fadeDelay * 2);
            $('div.bottom > div.left').width($('#container').data('left-width'));
            reinit();
        }
    });
}

function watchURLChange(){
    var tmploc = window.location + "";
    tmploc = tmploc.split('/');
    tmploc = tmploc[tmploc.length - 1];
    if (changing) {
        window.setTimeout("watchURLChange();", fadeDelay * 5);
    }
    else {
        if (loc !== tmploc) {
            animateOut();
            window.setTimeout(function(){
                animateIn('/' + tmploc);
            }, fadeDelay);
        }
        else {
            window.setTimeout("watchURLChange();", 80);
        }
    }
}

function resize(){
    var height = $(window).height();
    var width = $(window).width();
	$('#sidebar').css('left',$('#wrapper').position().left+750);
	if($('#sidebar').css('opacity') < 1){
		$('#sidebar').animate({
			opacity : 1
		}, 1000);
	}
    if (width > height && $("#bg img").height() > height) {
        $("#bg img").width(width);
        $("#bg img").height('auto');
    }
    else {
        $("#bg img").width('auto');
        $("#bg img").height(height);
    }
}

function initArtistType(){
    types = $('.artist-type > option');
    var imgSrc = $('#bg > img').attr('src')
    for (var i = 1; i < $(types).length; i++) {
        var img = document.createElement('IMG');
        var type = $(types[i]).val();
        img.setAttribute('id', type);
        img.setAttribute('src', imgSrc.replace('painter', type));
		$(img).ready(resize);
        $('#bg').append(img);
    }
    resize();
	$('.artist-type').val($('.artist-type').val());
    $('.artist-type').change(function(){
		$('.artist-type').addClass('filled-out');
        $('#bg > img.cur').animate({
            opacity: 0
        }, fadeDelay).removeClass('cur');
        var cur = $(this).val();
		$('.artist-type').not(this).val(cur);
        window.setTimeout(function(){
            $('#' + cur).animate({
                opacity: 1
            }, fadeDelay).addClass('cur');
        }, fadeDelay / 4);
		document.cookie = 'type:'+$(this).val();
    });
}

function submitEmailForm(e){
	email = $(e).siblings('.email');
	if ($(email).length == 0) {
		email = $(e).parent().parent().find('.email');
	}
    if (!$(email).val().match(/^\w+@\w+.\w+/)) {
        $(email).val("That's not valid...");
    }
    else {
        email = $(e).parent().parent('form');
        if(email.length < 1)
            email = $('#header-email-signup');
        else
            email = email[0];
        $.post('/email-signup', $(email).serialize(), function(data){
            $('#header > form').replaceWith(data);
        });
    }
}

function initEmailSubmit(){
    $('.email-signup').add($('.submit')).unbind();
    //	$('.email-signup').submit(function(event){
    //		event.preventDefault();
    //        submitEmailForm($(this));
    //    });
    $('.submit').bind('click', function(event){
        event.preventDefault();
        submitEmailForm($(this));
    });
}

function reinit(){
	initArtistType();
    //Current page = loc
    loc = window.location + "";
    loc = loc.split('/');
    loc = loc[loc.length - 1];
    if (loc == '') {
        var id = '#home';
    }
    else {
        var id = '#' + loc;
    }
    $(id).children().addClass('current-page');
    $('a:not(.no-link)').unbind('click');
    $('a:not(.no-link)').bind('click', function(event){
        changing = true;
        window.setTimeout("changing = false;", fadeDelay * 3);
        leave(event);
        nextPage = $(this).attr('href');
        if (nextPage == '') {
            nextPage = 'home';
        }
        if (Modernizr.history) {
            var stateObject = nextPage;
            window.history.pushState(stateObject, "", nextPage);
            if ($(this).attr('class') == 'bottom-link') {
                smoothScroll();
            }
        }
        else {
            window.location.href = nextPage;
        }
        window.setTimeout(function(){
            animateIn(nextPage);
			window.setTimeout("resize();", fadeDelay);
        }, fadeDelay * 3.5);
    });
	resize();
	window.setTimeout("resize();",fadeDelay*2);
}

function init(){
    resize();
    initEmailSubmit();
    reinit();
    watchURLChange();
    window.setTimeout("resize();", 200);
	if(document.cookie.match('type:')){
		var type = document.cookie.split(';');
		for (var i = 0; i < type.length; i++){
			if(type[i].match('type:')){
				type= type[i];
				break;
			}
		}
//		type = type[1]+'';
		type = type.replace('type:','');
		type = type.replace(' ','');
		type = type.replace('=','');
		$('.artist-type').val(type);
		$('.artist-type').change();
		   
    }
}
