jQuery.event.add(window, 'load', initDndi);
jQuery.event.add(window, 'unload', leave);

var date = new Date();
var aEnterTimer;
var inFocus = false;
var hoverTime = 1000;

function moveAddDiv(){
    $('#add-new-piece').attr('href', '#');
    //    $('#medium').prepend(document.getElementById('add-new-piece'));
    //    $('#other-images').prepend(document.getElementById('add-new-piece'));
    //	$('#add-new-piece').remove();
}

function showRequest(formData, jqForm, options){
    console.log('requesting...');
    
}

function handlePostSuccess(responseText, statusText, xhr, $form){
    console.log('handling success');
    var ajax = '/get/header';
    window.setTimeout(function(){
        $.get(ajax, function(data){
            $('#header').html(data);
        });
        ajax = '/get/' + loc;
        $.get(ajax, function(data){
            $('.content').remove();
            $('#container').html($('#container').html() + data);
        });
    }, 1500);
    window.setTimeout("dndiHeader();", 1550);
    $('#close-add-piece').trigger('click');
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
        url: '/add/piece',
        clearForm: true
    };
    $('#add-piece-form').submit(function(){
        if ($('#piece_title').val() == '') {
            console.log('title');
            $('#piece_title').css('background-color', '#900');
        }
        else if ($('#piece_default_image').val() == "") {
            console.log('image');
            $('#piece_default_image').css('background-color', '#F00');
        }
        else if ($('#piece_series').val() == '') {
            console.log('series');
            $('#piece_series').css('background-color', '#F00');
        }
        else {
            console.log('sending...');
            $('#add-piece-form').ajaxSubmit(options);
        }
        
        return false;
    });
}

function leave(){
    //	alert('epace');
}

function overA(obj){
    console.log(obj + '  over');
    date = new Date();
    if (aEnterTimer + hoverTime < date.getTime() && inFocus) {
        console.log('good to go');
        $(obj).css('border', '1px solid #F00');
        $(obj).unbind('click');
        $(document).bind('keydown', function(event){
            var key = event.which;
            if (key == null) 
                key = event.keyCode;
            if (key == 27) {
                $(document).unbind('mousemove');
                $(obj).css('border', 'none');
            }
        });
        $(document).bind('mousemove', function(e){
            console.log('down');
            $(obj).css('position', 'relative');
            $(obj).css('width', $(obj).width());
            $(obj).css('height', $(obj).height());
            console.log('mouseX: ' + e.pageX + ', objX: ' + $(obj).position().top);
            $(obj).offset({
                top: e.pageY - $(obj).height() / 2,
                left: e.pageX - $(obj).width()
            });
        });
    }
    else if (inFocus) {
        window.setTimeout(function(){
            overA(obj);
        }, hoverTime);
    }
}

function dndiHeader(){
    as = $('a');
    for (var i = 0; i < $(as).length; i++) {
        $(as[i]).attr('href', '/edit' + $(as[i]).attr('href'));
    }
    //    as = $('#header').children('a').add('#nav');
    for (var i = 0; i < $(as).length; i++) {
        $(as[i]).hover(function(){
            console.log('entered...');
            date = new Date();
            aEnterTimer = date.getTime();
            inFocus = true;
            overA(this);
        }, function(){
            //unbind the dndi
            inFocus = false;
        });
        //        $(as[i]).bind('mouseover', overA(as[i]));
    }
}

function initDndi(){
    dndiHeader();
    moveAddDiv();
    initAddNew();
}
