jQuery.event.add(window, 'load', initVideos);

function youtube(data){
    var videos = data;
//	console.log(videos);
    videos = videos.feed;
    videos = videos.entry;
//    $('#container > div.profile > img').attr('src', $(videos[0]).attr('user_portrait_huge'));
//    $('#container > div.profile > h3').text('Vimeo profile: ' + $(videos[0]).attr('user_name'));
    for (var i = 0; i < $(videos).length; i++) {
        var container = document.getElementById('container');
        var div = document.createElement('DIV');
        var iframe = document.createElement('IFRAME');
		var tmp = $($(videos[i])[0]).attr('id');
		tmp = $(tmp).attr('$t');
		tmp = tmp.split('/')[tmp.split('/').length -1 ]; 
        iframe.src = 'http://www.youtube.com/embed/' + tmp;
        div.setAttribute('class', 'video-div');
        var p = document.createElement('P');
        var a = document.createElement('A');
		tmp = videos[i].link[0].href;
		console.log(videos[i]);
//        tmp = $(tmp).attr('href');
        a.setAttribute('href', tmp);
        a.setAttribute('target', '_blank');
		tmp = videos[i].title;
		tmp = tmp.$t;
//		tmp = $(tmp).attr('href');
        a.innerHTML = tmp + '<br/><br/>';
		tmp = videos[i].content;
        tmp = tmp.$t;
        p.innerHTML = tmp + '<br/>';
        div.appendChild(a);
        div.appendChild(iframe);
        div.appendChild(p);
        container.appendChild(div);
    }
}

function vimeo(data){
    console.log(data);
    var videos = $(data);
    $('#container > div.profile > img').attr('src', $(videos[0]).attr('user_portrait_huge'));
    $('#container > div.profile > h3').text('Vimeo profile: ' + $(videos[0]).attr('user_name'));
    for (var i = 0; i < $(videos).length; i++) {
        var container = document.getElementById('container');
        var div = document.createElement('DIV');
        var iframe = document.createElement('IFRAME');
        iframe.src = 'http://player.vimeo.com/video/' + $(videos[i]).attr('id');
        div.setAttribute('class', 'video-div');
        var p = document.createElement('P');
        var a = document.createElement('A');
        a.setAttribute('href', $(videos[i]).attr('url'));
        a.setAttribute('target', '_blank');
        a.innerHTML = $(videos[i]).attr('title') + '<br/><br/>';
        p.innerHTML = $(videos[i]).attr('description') + '<br/>';
        div.appendChild(a);
        div.appendChild(iframe);
        div.appendChild(p);
        container.appendChild(div);
    }
}
function initVideos(){
    var url = 'https://gdata.youtube.com/feeds/api/videos?author=hcwiley&alt=json&prettyprint=true';
    $.get(url, function(data){
        youtube(data);
    });
    var url = 'http://vimeo.com/api/v2/hcwiley/all_videos.json?callback=?';
	$.getJSON(url, function(data){
        vimeo(data);
    });
}
