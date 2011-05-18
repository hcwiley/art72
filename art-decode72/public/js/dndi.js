jQuery.event.add(window, 'load', initDndi);
jQuery.event.add(window, 'unload', leave);

function moveAddDiv(){
    $('#add-new-piece').attr('href', '#');
    $('#medium').prepend(document.getElementById('add-new-piece'));
    $('#other-images').prepend(document.getElementById('add-new-piece'));
    //	$('#add-new-piece').remove();
}

function showRequest(){
	console.log('requesting...');

}

function handlePostSuccess(){
	console.log('handling success');
    var ajax = '/get/header';
    window.setTimeout(function(){
        $.get(ajax, function(data){
            $('#header').html(data);
        });
    }, 1500);
}

function handlePostFail(){
    alert('sorry something went wrong...');
}

function initAddNew(){
    $('#close-add-piece').bind('click', function(){
        $('#add-piece').animate({
            opacity: 0
        }, 100);
        $('#add-piece').css('z-index', -1);
    });
    $('#add-new-piece').bind('click', function(){
        $('#add-piece').animate({
            opacity: 1
        }, 100);
        $('#add-piece').css('z-index', 2);
    });
    var options = {
//        target: '#header', // target element(s) to be updated with server response 
        beforeSubmit: showRequest, // pre-submit callback 
        success: handlePostSuccess, // post-submit callback
        url: '/add/piece'
    };
    $('#submit-piece').bind('click', function(){
		console.log('sending...');
        $('#add-piece-form').ajaxSubmit(function(options){
			return false;
        });
    });
}

function leave(){
    //	alert('epace');
}

function initDndi(){
    as = $('a');
    for (var i = 0; i < $(as).length; i++) {
        $(as[i]).attr('href', '/edit' + $(as[i]).attr('href'));
    }
    moveAddDiv();
    initAddNew();
}
