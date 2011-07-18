jQuery.event.add(window, 'load', initEdit);
//jQuery.event.add(window, 'unload', leavingPage);
var changesMade = false;

function unloadPage(){
    if (changesMade) {
        return "Leave page without saving changes?";
    }
}

window.onbeforeunload = unloadPage;

function leavingPage(){
    if (changesMade) {
        if (confirm('Leave page without saving changes?')) {
            alert('you hit ok');
        }
        else {
            saveChanges();
        }
    }
}

function saveChanges(){
    //console.log('saving changes');
}

function moveAddDiv(){
    $('#gallery').prepend(document.getElementById('add-new-piece'));
    $('#series').prepend(document.getElementById('add-new-piece'));
    $('#other-images').prepend(document.getElementById('add-new-piece'));
    $('#add-new-piece').animate({
        opacity: 1
    }, 800);
}

function showRequest(formData, jqForm, options){
    ////console.log('requesting...');
}

function handlePostSuccess(responseText, statusText, xhr, $form){
    ////console.log('handling success');
    var ajax = '/get/header';
    window.setTimeout(function(){
        $.get(ajax, function(data){
            $('#header').html(data);
        });
        ajax = '/get/' + loc;
        $.get(ajax, function(data){
            $('#container').prepend($('#add-new-piece'));
            $('.content').remove();
            $('#container').html($('#container').html() + data);
            moveAddDiv();
            if (loc != 'edit') 
                initPieceGallery();
        });
    }, 1500);
    closeAddPieceForm();
}

function handlePostFail(){
    alert('sorry something went wrong...');
}

function closeAddSeriesForm(){
    $('#add-series').animate({
        opacity: 0
    }, 100);
    $('#add-series').css('z-index', -1);
}

function closeAddPieceForm(){
    $('#add-piece').animate({
        opacity: 0
    }, 100);
    $('#add-piece').css('z-index', -1);
}

function editHeader(){
    as = $('a');
    for (var i = 0; i < $(as).length; i++) {
        $(as[i]).attr('href', '/edit' + $(as[i]).attr('href'));
    }
}

function initAddNew(){
    $('#close-add-piece').bind('click', function(){
        closeAddPieceForm();
    });
    $('#close-add-series').bind('click', function(){
        closeAddSeriesForm();
    });
    $('#add-new-series').bind('click', function(){
        $('#add-series').animate({
            opacity: 1
        }, 100);
        $('#add-series').css('z-index', 3);
    });
    $('#add-new-piece').bind('click', function(){
        $('#add-piece').animate({
            opacity: 1
        }, 100);
        $('#add-piece').css('z-index', 3);
    });
    var options = {
        //        target: '#header', // target element(s) to be updated with server response 
        beforeSubmit: showRequest, // pre-submit callback 
        success: handlePostSuccess, // post-submit callback
        //        url: '/add/piece',
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
            ////console.log('title');
            $('#piece_title').css('background-color', '#900');
        }
        else if ($('#piece_default_image').val() == "") {
            ////console.log('image');
            $('#piece_default_image').css('background-color', '#F00');
        }
        else if ($('#piece_series').val() == '') {
            ////console.log('series');
            $('#piece_series').css('background-color', '#F00');
        }
        else {
            ////console.log('sending...');
            $('#add-piece-form').ajaxSubmit(options);
        }
        
        return false;
    });
    var options = {
        //        target: '#header', // target element(s) to be updated with server response 
        beforeSubmit: showRequest, // pre-submit callback 
        success: handlePostSuccess, // post-submit callback
        //        url: '/add/series',
        clearForm: true
    };
    $('#add-series-form').bind('keypress', function(event){
        if (event.keyCode == 13 || event.which == 13) {
            $(this).trigger('submit');
        }
        else if (event.keyCode == 27 || event.which == 27) {
            closeAddPieceForm();
        }
    });
    $('#add-series-form').submit(function(){
        if ($('#series_name').val() == '') {
            ////console.log('title');
            $('#series_name').css('background-color', '#900');
        }
        else {
            ////console.log('sending...');
            $('#add-series-form').ajaxSubmit(options);
        }
        
        return false;
    });
}

function handleLogoutSuccess(){
    window.location = window.location;
}

function handleLogoutFail(){

}

function handleLoginSuccess(){
    window.location = window.location;
}

function handleLoginFail(response, statusText, xhr){
    ////console.log(response.responseText);
    if (response.responseText == 'password') {
        $('#login').html($('#login').html() + 'password did not match');
    }
    else if (response.responseText == 'username') {
        $('#login').html($('#login').html() + 'username not found');
    }
}

function initLogin(){
    $('#login-form').bind('keypress', function(event){
        if (event.keyCode == 13 || event.which == 13) {
            $(this).trigger('submit');
        }
        else if (event.keyCode == 27 || event.which == 27) {
            closeAddPieceForm();
        }
    });
    $('#login-form').submit(function(){
        if ($('#username').val() == '') {
            $('#username').css('background-color', '#900');
        }
        else if ($('#password').val() == "") {
            $('#password').css('background-color', '#F00');
        }
        else {
            ////console.log('sending...');
            $.ajax({
                url: '/login',
                type: 'POST',
                data: $('#login-form').serialize(),
                success: handleLoginSuccess,
                error: handleLoginFail
            });
        }
        
        return false;
    });
    $('#logout').click(function(){
        $.ajax({
            url: '/logout',
            type: 'POST',
            success: handleLogoutSuccess,
            error: handleLogoutFail
        });
    })
}

function checkAs(){
    as = $('.content > * > a');
    for (var i = 0; i < $(as).length; i++) {
        if (($(as[i]).attr('href') + '').substring(0, 5) != '/edit') 
            $(as[i]).attr('href', '/edit' + $(as[i]).attr('href'));
    }
}

function initEditable(){
    $('#logo>h2').mousedown(function(event){
        if (event.which == 3) {
            $(document)[0].oncontextmenu = function(){
                return false;
            }
            var p = prompt('What should be display here:', $(this).text());
            if ($(this).text() !== p) {
                changesMade = true;
                $('#save-menu').show();
                $(this).text(p);
                $('#logo').addClass('edited');
            }
        }
    });
    var links = $('#contact-links>a');
    for (var i = 0; i < $(links).length; i++) {
        $(links[i]).mousedown(function(event){
            if (event.which == 3) {
                $(document)[0].oncontextmenu = function(){
                    return false;
                }
                window.setTimeout("$('#shown').focus();", 2);
                $('#shown').val($(this).text());
                $('#linked').val($(this).attr('title'));
                $(this).parent('div').append($('#add-contact-info').show());
                $('#add-contact-info> .submit').click(function(){
                    //console.log('saved');
                    var link = $('#linked').val() + '';
                    if (link.search('@') !== -1) {
                        if (confirm('Is that an email address?')) {
                            type = 'email';
                        }
                    }
                    else if (link.search('http') !== -1) {
                        type = 'webpage';
                    }
                    else if (link.search(/\d{3}\W{1}\d{3}\W{1}\d{4}/g) !== -1 || link.search(/\d{10}/g) !== -1 || $('#shown').val().toLowerCase().search('phone') !== -1) {
                        if (confirm('Is that a phone number?')) {
                            type = 'phone';
                        }
                    }
                    else {
                        if (confirm('Is that a webpage?')) {
                            type = 'webpage';
                        }
                    }
                    $(links[i]).text($('#shown').val());
                    $(links[i]).attr('title', $('#linked').val());
                    $(links[i]).attr('href', link);
                    changesMade = true;
                    $('#save-menu').show();
					$(links[i]).data('type', type);
					$(links[i]).data('link', link);
                    $(links[i]).addClass('edited');
                    $('#container').prepend($('#add-contact-info').hide());
                    $('#add-contact-info> *').unbind('click');
                });
                $('#add-contact-info> .cancel').click(function(){
                    $('#container').prepend($('#add-contact-info').hide());
                    $('#add-contact-info> *').unbind('click');
                });
            }
        });
    }
    $('#add-new-contact>*').bind('click', function(){
        $('#add-new-contact>*').hide();
        $('#shown').val('');
        $('#linked').val('');
        $('#add-new-contact').append($('#add-contact-info').show());
        $('#shown').focus();
        $('#add-contact-info> .submit').click(function(){
            //console.log('saved');
            var a = document.createElement('A');
            var link = $('#linked').val() + '';
            if (link.search('@') !== -1) {
                if (confirm('Is that an email address?')) {
                    link = 'mailto:' + link;
                    type = 'email';
                }
                else 
                    link = link;
            }
            else if (link.search('http') !== -1) {
                link = link;
                type = 'webpage';
            }
            else if (link.search(/\d{3}\W{1}\d{3}\W{1}\d{4}/g) !== -1 || link.search(/\d{10}/g) !== -1 || $('#shown').val().toLowerCase().search('phone') !== -1) {
                if (confirm('Is that a phone number?')) {
                    link = 'callto://' + link;
                    type = 'phone';
                }
                else 
                    link = link;
            }
            else {
                if (confirm('Is that a webpage?')) {
                    link = 'http://' + link;
                    type = 'webpage';
                }
                else 
                    link = link;
            }
            a.setAttribute('href', link);
            a.setAttribute('target', '_blank');
            a.setAttribute('class', 'edited');
            a.innerText = $('#shown').val();
            document.getElementById('contact-links').appendChild(a);
            changesMade = true;
            $(a).data('type', type);
			$(a).data('link', link);
            $('#save-menu').show();
            $('#add-new-contact>p').show();
            $('#container').prepend($('#add-contact-info').hide());
            $('#add-contact-info> *').unbind('click');
        });
        $('#add-contact-info> .cancel').click(function(){
            $('#add-new-contact>p').show();
            $('#container').prepend($('#add-contact-info').hide());
            $('#add-contact-info> *').unbind('click');
        });
    });
}


function saveMenu(){
    $('#save').bind('click', function(){
        //console.log('saving...');
        var edited = $('.edited');
        for (var i = 0; i < $(edited).length; i++) {
            if ($(edited[i]).attr('id') == 'logo') {
                $(edited[i]).removeClass('edited');
                $.ajax({
                    type: 'POST',
                    url: '/save/logo',
                    data: {
                        logo: $('#logo > h2').text(),
                        user: $('#user-menu>p>strong').text()
                    },
                    success: function(data){
                        //console.log(data);
                    },
                });
            }
            else if (loc == 'contact' && $(edited[i]).parent('div').attr('id') == 'contact-links') {
                $("#contact-links> .edited").removeClass('edited');
                //console.log($("#contact-links").html());
                $.ajax({
                    type: 'POST',
                    url: '/save/contact',
                    dataType: 'HTML',
                    data: {
                        displayed: $(edited[i]).text(),
                        type: $(edited[i]).data('type'),
                        link: $(edited[i]).attr('href'),
                        user: $('#user-menu>p>strong').text()
                    },
                    success: function(data){
                        //console.log(data);
                    },
                });
            }
        }
        changesMade = false;
        $('#save-menu').hide();
    });
    $('#reset').bind('click', function(){
        changesMade = false;
        window.location = window.location;
    });
}


function initEdit(){
    moveAddDiv();
    checkAs();
    initAddNew();
    initLogin();
    initEditable();
    saveMenu();
    if (loc != 'edit') 
        $('#piece_series').val(loc)
    else {
        $('.gallery_thumb').removeClass('gallery_thumb');
    }
}
