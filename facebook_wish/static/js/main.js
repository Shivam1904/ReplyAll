$(function() {

    // Submit post on submit
    $('#dataform').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
    });

    // AJAX for posting
    function create_post() {
        console.log("create post is working!") // sanity check
        var key1 = $('#keyword').val();
        var sel1 ='' ;
        $('#sell :selected').each(function(i, selected){
            if(sel1 == '')
                sel1 = $(selected).val();
            else
                sel1 = sel1+','+$(selected).val();
        });
        var sub1 = $('#subscriber').val();
        var view1 = $('#views').val();
        var start1 = $('#startdate').val();
        var end1 = $('#enddate').val();
        alert(key1+' '+sel1+' '+sub1+' '+view1+' '+end1+' '+start1  );
        $.ajax({
            url : "/formsubmit/", // the endpoint
            type : "POST", // http method
            data : {keyword:key1, category:sel1, subscriber:sub1,viewcount:view1,enddate:start1,startdate:end1}, // data sent with the post request
            // handle a successful response
            success : function(json) {
                readTextFile('/data');
                console.log("success yay"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
               alert("error");
               console.log(xhr.status + ": " + xhr.responseText);  
                            }
        });
    };

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    
    // The functions below will create a header with csrftoken
    

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    
        function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});