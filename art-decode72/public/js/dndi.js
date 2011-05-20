jQuery.event.add(window, 'load', initDndi);
jQuery.event.add(window, 'unload', leave);

var date = new Date();
var aEnterTimer;
var inFocus = false;
var hoverTime = 1500;

function moveAddDiv(){
    $('.content').prepend(document.getElementById('add-new-piece'));
    $('#add-new-piece').animate({
        opacity: 1
    }, 800);
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
    closeAddPieceForm();
}

function handlePostFail(){
    alert('sorry something went wrong...');
}

function closeAddPieceForm(){
    $('#add-piece').animate({
        opacity: 0
    }, 100);
    $('#add-piece').css('z-index', -1);
}

function initAddNew(){
    $('#close-add-piece').bind('click', function(){
        closeAddPieceForm();
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
    $('#add-piece-form').bind('keypress', function(event){
        if (event.keyCode == 13 || event.which == 13) {
            $(this).trigger('submit');
        }
        else if (event.keyCode == 27 || event.which == 27) {
            closeAddPieceForm();
        }
    });
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
    console.log($(obj).attr('id') + '  over');
    date = new Date();
    if (aEnterTimer + hoverTime < date.getTime() && inFocus && $('.editting').length == 0) {
        console.log('good to go');
        $(obj).addClass('editting');
        var helpText = document.createElement('h4');
        helpText.innerHTML = 'press enter to start placing';
        $(helpText).attr('id', 'help-text');
        $(obj).prepend(helpText);
        $(obj).children('img').css('z-index', '0');
        lastHref = $(obj).attr('href');
        $(obj).attr('href', '#');
        $(document).bind('keydown', function(event){
            var key = event.which;
            if (key == null) 
                key = event.keyCode;
            if (key == 27) {
                $(document).unbind('');
                $(obj).removeClass('editting');
                $(obj).attr('href', lastHref);
                $('#help-text').remove();
                inFocus = false;
            }
            else if (key == 13) {
                $(document).bind('mousemove', function(e){
                    console.log('down');
                    $(helpText).text('press esc to stop placing');
                    $(obj).css('width', $(obj).width());
                    $(obj).css('height', $(obj).height());
                    console.log('mouseX: ' + e.pageX + ', objX: ' + $(obj).position().top);
                    $(obj).offset({
                        top: e.pageY - $(obj).height() / 2,
                        left: e.pageX - $(obj).width() / 2
                    });
                });
            }
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
    as = $('#header').add('#nav').add('#contact').add('#logo').add('#container');
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

function saveMenu(){
    $('#save').bind('click', function(){
        var header = 'width=' + $('#header').width() + 'px&height=' + $('#header').height() + 'px&';
        header += 'left=' + $('#header').position().left + 'px&top=' + $('#header').position().top + 'px&'&
        var nav = 'nav@width=' + $('#nav').width() + 'px&height=' + $('#nav').height() + 'px&'&
        nav += 'left=' + $('#nav').position().left + 'px&top=' + $('#nav').position().top + 'px&'&
        var contact = 'contact@width=' + $('#contact').width() + 'px&height=' + $('#contact').height() + 'px&'&
        contact += 'left=' + $('#contact').position().left + 'px&top=' + $('#contact').position().top + 'px&'&
        var logo = 'logo@width=' + $('#logo').width() + 'px&height=' + $('#logo').height() + 'px&'&
        logo += 'left=' + $('#logo').position().left + 'px&top=' + $('#logo').position().top + 'px&'&
        var container = 'container@width=' + $('#container').width() + 'px&height=' + $('#container').height() + 'px&'&
        container += 'left=' + $('#container').position().left + 'px&top=' + $('#container').position().top + 'px&'&
        console.log('header css\n' + header);
        console.log('nav css\n' + nav);
        console.log('logo css\n' + logo);
        console.log('contact css\n' + contact);
        console.log('container css\n' + container);
        $.ajax({
            type: 'POST',
            url: '/save/css',
            data: header,
            success: function(data){
                console.log(data);
            },
        });
    });
}

function initDndi(){
    dndiHeader();
    moveAddDiv();
    initAddNew();
    saveMenu();
}
