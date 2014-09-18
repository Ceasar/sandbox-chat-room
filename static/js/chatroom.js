var pusher = new Pusher('ceb9e10775a1d1de32b6')
var channel = pusher.subscribe('test_channel');
channel.bind('test_event', function(data) {
    $('.messages').append("<p>" + data.message + "</p>");
});

// Include CSRF Token on cross domain requests
// https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ajax
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$("form").submit(function(e) {
    e.preventDefault();
    var message = $(".message-input").val();
    $.ajax({
        type: "POST",
        url: "/messages",
        data: {
            "message": message,
        },
        dataType: "json",
    });
});

$('.message-input').focus();
