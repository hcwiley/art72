jQuery.event.add(window, 'load', initVideos);

function youtube(data){
    var videos = data;
    videos = videos.feed;
    videos = videos.entry;
    var profile = $('.profile.original').clone();
    $(profile).removeClass('original');
    $(profile).addClass('youtube');
    $(profile).children('div.info').children('a').attr('href', 'http://youtube.com/' + videos[0].author[0].name['$t']);
    $(profile).children('div.info').children('a').children('img').attr('src', data.feed.logo['$t']);
    $(profile).children('div.info').children('a').children('h4').text('Youtube profile: ' + videos[0].author[0].name['$t']);
    for (var i = 0; i < $(videos).length; i++) {
        var div = $(profile).children('.original').clone();
        $(div).removeClass('original');
        var tmp = $($(videos[i])[0]).attr('id');
        tmp = tmp.$t;
        tmp = tmp.split('/')[tmp.split('/').length - 1];
        tmp = 'http://www.youtube.com/embed/' + tmp;
        $(div).children('iframe').attr('src', tmp);
        tmp = videos[i].link[0].href;
        $(div).children('a').attr('href', tmp);
        $(div).children('a').attr('target', '_blank');
        tmp = videos[i].title;
        tmp = tmp.$t;
        $(div).children('a').text(tmp);
        tmp = videos[i].content;
        tmp = tmp.$t;
        $(div).children('p.description').html(tmp);
        $(profile).append(div);
    }
    $('#container').append(profile);
}

function vimeo(data){
    //    console.log(data);
    var videos = $(data);
    var profile = $('.profile.original').clone();
    $(profile).removeClass('original');
    $(profile).addClass('vimeo');
    $(profile).children('div.info').children('a').attr('href', $(videos[0]).attr('user_url'));
    $(profile).children('div.info').children('a').children('img').attr('src', $(videos[0]).attr('user_portrait_large'));
    $(profile).children('div.info').children('a').children('h4').text('Vimeo profile: ' + $(videos[0]).attr('user_name'));
    for (var i = 0; i < $(videos).length; i++) {
        var div = $(profile).children('.original').clone();
        $(div).removeClass('original');
        $(div).children('iframe').attr('src', 'http://player.vimeo.com/video/' + $(videos[i]).attr('id'));
        $(div).children('a').attr('href', $(videos[i]).attr('url'));
        $(div).children('a').attr('target', '_blank');
        $(div).children('a').text($(videos[i]).attr('title'));
        $(div).children('p.description').html($(videos[i]).attr('description'));
        $(profile).append(div);
    }
    $('#container').append(profile);
}

function initVideos(){
    $('#video-username').keydown(function(event){
		if (event.which == 13 || event.keyCode == 13) {
			var username = $('#video-username').val(); 
			//	username = prompt('Whats you youtube username?','');
			var url = 'https://gdata.youtube.com/feeds/api/videos?author=' + username + '&alt=json&prettyprint=true';
			$.get(url, function(data){
				youtube(data);
			});
			//	username = prompt('Whats you vimeo username?','');
			var url = 'http://vimeo.com/api/v2/' + username + '/all_videos.json?callback=?';
			$.getJSON(url, function(data){
				vimeo(data);
			});
		}
	});
    $('#select-all').bind('click', function(){
        $('input:[type=checkbox]').attr('checked', true);
    });
    $('#deselect-all').bind('click', function(){
        $('input:[type=checkbox]').attr('checked', false);
    });
    $('#add-to-profile').bind('click', function(){
        var vids = $('input:[checked=true]');
        for (var i = 0; i < $(vids).length; i++) {
            var form = $('#add-video-form').clone();
            $(form).children('[name=title]').val($(vids[i]).siblings('a').text());
            $(form).children('[name=url]').val($(vids[i]).siblings('iframe').attr('src'));
            $.post('/add/video', $(form).serialize(), function(request, status, xhr){
				$('#video-menu').html($('#video-menu').html()+"<br/>"+request);
            });
        }
    });
}
