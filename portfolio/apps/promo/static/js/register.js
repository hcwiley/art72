jQuery.event.add(window, 'load', initRegister);
//Variable to control how long it takes to scroll up and down
var scrollTime = 700;
var steps;

function initPreview(){
	$('#close-preview').unbind('click');
    $('#close-preview').click(function(){
        var width = $(window).width();
        var height = $(window).height();
        $('#dark-overlay').add($('#preview')).animate({
            top: height / 2,
            left: width / 2,
            width: 0,
            height: 0,
        }, scrollTime);
        window.setTimeout(function(){
            $('#dark-overlay').add($('#preview')).css('display', 'none');
        }, scrollTime);
    });
    var previews = $('.preview');
    for (var i = 0; i < $(previews).length; i++) {
		$(previews[i]).unbind('click');
        $(previews[i]).bind('click', function(){
            $('#preview').add($('#dark-overlay')).css('display', 'block');
            var width = $(window).width();
            var height = $(window).height();
            $('#dark-overlay').add($('#preview')).css({
                'top': height / 2,
                'left': width / 2,
            });
            $('#dark-overlay').animate({
                top: 0,
                left: 0,
                width: '100%',
                height: '100%',
            }, scrollTime);
            var scale = .8
            $('#preview').animate({
                top: (height - height * scale) / 2,
                left: (width - width * scale) / 2,
                width: (width * scale),
                height: (height * scale),
            }, scrollTime);
			var url = 'http://hcwiley.com';
            $('#preview > #page').attr('data',url);
            $('#preview > #page > embed').attr('src',url);
			/*The call i'm going to make
            $.post('/render-preview', $('#render-me').serialize(), function(){
                $('#preview > #page').html(data);
            });
            */
        });
    }
}

function initSideBarScroll(){
    $('#sidebar').bind('mouseenter', function(){
        $(window).bind('mousemove', function(event){
            if (event.pageY < 120 || event.clientY < 120) {
                $('#sidebar > div').stop(true,false).animate({
                    top: 0
                }, 400);
            }
            else if (event.pageY > $(window).height() - 120 || event.clientY > $(window).height() - 120) {
                $('#sidebar > div').stop(true,false).animate({
                    top: $('#sidebar > div').height() - $('#sidebar').height() - 100
                }, 400);
            }
        });
    });
    $('#sidebar').bind('mouseleave', function(){
        $(window).unbind('mousemove');
    });
}

function initSteps(){
    steps = $('div.step');
    for (var i = 0; i < $(steps).length; i++) {
        $(steps[i]).click(function(){
            if ($(this).attr('class').match('completed-step')) {
                if ($(this).attr('id') == 's' + 0) {
                    $('#central-register').animate({
                        top: 0
                    }, scrollTime);
                    $('#plan').show();
                    $('#central-register > div:not(#plan)').hide();
                }
                else if ($(this).attr('id') == 's' + 1) {
                    $('#central-register').animate({
                        top: -600
                    }, scrollTime);
                    $('#sidebar > div').animate({
                        top: 0
                    }, scrollTime);
                    $('#create-account').show();
                    $('#central-register > div:not(#create-account)').hide();
                }
                else if ($(this).attr('id') == 's' + 2) {
                    $('#central-register').animate({
                        top: -600
                    }, scrollTime);
                    $('#layout').show();
                    $('#central-register > div:not(#layout)').hide();
                }
            }
        });
    }
}

function initSelect(){
    var selects = $('.select');
    for (var i = 0; i < $(selects).length; i++) {
        $(selects[i]).click(function(){
            //For Layout thirds selection button
            if ($(this).parent('div').parent('div').attr('class') == 'layout-thirds') {
                if ($(steps[2]).children('div').children('.progress-feedback').length > 0) {
                    $(steps[2]).children('div').children('.progress-feedback').remove();
                }
                $('#layout-input').val($(this).siblings('h4').text());
                $(steps[2]).children('div').html($(steps[2]).children('div').html() + '<h6 class="progress-feedback"><br> -- ' + $(this).siblings('h4').text() + ' selected</h6>');
                var img = $(this).parent('div').siblings('img').clone();
                img.addClass('progress-feedback');
                $(steps[2]).children('div').append(img);
                img = $(this).parent('div').siblings('p.preview').clone();
                img.addClass('progress-feedback');
                $(steps[2]).children('div').append(img);
                $(this).parent('div').parent('div').parent('div').parent('div').addClass('collapse').next('div').children('h3:first').trigger('click');
            }
            //Color option select button
            else if ($(this).parent('div').attr('class') == 'color-option') {
                if ($(steps[2]).children('div').children('.progress-feedback-color').length > 0) {
                    $(steps[2]).children('div').children('.progress-feedback-color').remove();
                }
                $('#color-input').val($(this).siblings('img').attr('alt'));
                $(steps[2]).children('div').html($(steps[2]).children('div').html() + '<h6 class="progress-feedback-color"><br/> -- ' + $(this).siblings('img').attr('alt') + ' selected</h6>');
                var img = $(this).siblings('img').clone();
                img.addClass('progress-feedback-color');
                $(steps[2]).children('div').append(img);
                img = $(this).siblings('p.preview').clone();
                img.addClass('progress-feedback-color');
                $(steps[2]).children('div').append(img);
                $(this).parent('div').parent('div').parent('div').addClass('collapse').next('div').children('h3:first').trigger('click');
            }
            //font options select button
            else if ($(this).parent('div').attr('class') == 'font-options') {
                if ($(steps[2]).children('div').children('.progress-feedback-font').length > 0) {
                    $(steps[2]).children('div').children('.progress-feedback-font').remove();
                }
                $(steps[2]).children('div').html($(steps[2]).children('div').html() + '<h6 class="progress-feedback-font"><br/> -- and your fonts<br/></h6>');
                var img = $(this).parent('div').clone();
                $('#font-input').val($(img).attr('alt'));
                img.addClass('progress-feedback-font');
                img.children('.select').remove();
                $(steps[2]).children('div').append(img);
            }
            //Check sidebar position
            var diff = ($('#sidebar').height() - 200) - $('#sidebar > div').height();
            if (diff < 0) {
                $('#sidebar > div').animate({
                    top: diff
                }, scrollTime);
            }
			initPreview();
        });
    }
}

function initRegister(){
    $('#sidebar').data('lastHeight', 0);
    initSteps();
    initSelect();
	$('#account-form input').focus(function(){
		$(this).addClass('filled-out');
	});
    $('div.plan-button').bind('click', function(){
        $('#central-register').animate({
            'top': '-=' + ($('#plan').height() + 600)
        }, scrollTime);
        $(steps[1]).addClass('completed-step');
        if ($(steps[0]).children('div').find('.progress-feedback').length > 0) {
            $(steps[0]).children('div').find('.progress-feedback').remove();
        }
        $(steps[0]).children('div').html('<h6 class="progress-feedback"><br/> -- ' + $(this).siblings('h3').text() + ' plan choosen</h6>');
        $('#create-account').show();
    });
    $('#account-done').bind('click', function(){
		if (!location.host.match('blu-wired')) {
			//Validate form
			if (!$('#account-form input[name="first_name"]').val().match(/^\w+/)) {
				$('#account-form input[name="first_name"]').focus();
				$('#form-feedback > *').text("You forgot your first name...");
				return;
			}
			if (!$('#account-form input[name="last_name"]').val().match(/^\w+/)) {
				$('#account-form input[name="last_name"]').focus();
				$('#form-feedback > *').text("You forgot your last name...");
				return;
			}
			else if (!$('#account-form input[name="email"]').val().match(/^\w+@\w+.\w+/)) {
				$('#account-form input[name="email"]').focus();
				$('#form-feedback > *').text("That's not a valid email...");
				return;
			}
			else if (!$('#account-form input[name="password"]').val().match(/^\w{6}/)) {
				$('#account-form input[name="password"]').focus();
				$('#form-feedback > *').html("Your password must be<br/>at least 6 characters");
				return;
			}
			else if ($('#account-form input[name="password"]').val() != $('#account-form input[name="confirm_password"]').val()) {
				$('#account-form input[name="confirm_password"]').focus();
				$('#form-feedback > *').html("Your password does not match");
				return;
			}
			else if (!$('#account-form input[name="terms"]').attr('checked')) {
				$('#account-form input[name="terms"]').focus();
				$('#form-feedback > *').html("You must agree to the terms of service");
				return;
			}
			//Submit form
			var ajax = $.ajax({
				type: 'POST',
				url: '/create-account',
				data: $('#account-form').serialize(),
				success: function(data){
					alert('yes!');
				},
				error: function(data){
					$('#form-feedback > *').html('sorry that didnt work');
					alert('this just comes up to prevent the page for a minute, in the future it will not continue if the form doesnt validate server side');
				}
			});
		}
        $('#central-register').animate({
            'top': '-=' + ($('#create-account').height() + 600)
        }, scrollTime);
        $(steps[2]).addClass('completed-step');
        $('#layout').show();
    });
    $('div.layout-options > h3').click(function(){
        if ($(this).parent('div').attr('class').match('collapse')) {
            $(this).parent('div').removeClass('collapse');
        }
        else {
            $(this).parent('div').addClass('collapse');
        }
    });
//    $('div.plan-button:last').trigger('click');
//    $('#account-done').trigger('click');
//	$('p.preview:first').trigger('click');
	$('head').append($('#register-css'));
    initSideBarScroll();
    initPreview();
}
