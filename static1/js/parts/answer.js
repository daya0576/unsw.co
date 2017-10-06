//delete answer
function delete_answer(answer_id){
    if(window.confirm('Are u sure to delete this answer ?')){
        $.getJSON('/rango/delete_answer/', {answer_id: answer_id}, function(data){
            return_code = data['return_code'];
            if(return_code == 1){
                alert('Answer has been deleted successfully!');
                location.reload();
            }else{
                alert("Something goes wrong, page does not be deleted.")
            }
        });
    }
}

function show_editor(obj, answer_id){

    $("#answer_content"+answer_id).html("<img scr='/images/favicon.ico'></img>");
    $.get('/rango/edit_answer/', {answer_id: answer_id}, function(data){
//        $("#answer_content"+answer_id).html(data);
//        $("#answer_content"+answer_id).load("/rango/edit_description_view/?answer_id=9");
//        $("#answer_content"+answer_id).html('<script id="container" name="content" type="text/plain">这里写你的初始化内容</script>')
        $(".cat_content").html('<script id="container" name="content" type="text/plain">这里写你的初始化内容</script>')
    });
}


var test;
function button_up_css_on(obj){
    $(obj).css("background-color", "#337ab7");
    $(obj).css("color", "#fff");
    $(obj).children(".vote-arrow").css("border-bottom-color", "white");
    $(obj).attr("aria-pressed", "true");
}
function button_up_css_off(obj){
    $(obj).css("background-color", "#efefef");
    $(obj).css("color", "#337ab7");
    $(obj).children(".vote-arrow").css("border-bottom-color", "#337ab7");
    $(obj).attr("aria-pressed", "false");
}
function button_down_css_on(obj){
    $(obj).css("background-color", "#337ab7");
    $(obj).children(".vote-arrow").css("border-top-color", "white");
    $(obj).attr("aria-pressed", "true");
}
function button_down_css_off(obj){
    $(obj).css("background-color", "#efefef");
    $(obj).children(".vote-arrow").css("border-top-color", "#337ab7");
    $(obj).attr("aria-pressed", "false");
}


function answer_up(answer_id, obj){
    $.getJSON('/rango/answer_up/', {answer_id: answer_id}, function(data){
        var return_code = data['return_code'];
        var likes_count = data['likes_count'];
        var likes_person = data['likes_person'];

        if(return_code == 1){
            $(obj).children(".count").html(likes_count);
            $(obj).parents('div[class^="cell"]').find(".likes_person").html(likes_person)
            alert('Thanks for your support!');
        }else{
            alert("Something goes wrong. Sorry, try again.")
            location.reload();
        }
    });
}
function answer_up_off(answer_id, obj){
    $.getJSON('/rango/answer_up_off/', {answer_id: answer_id}, function(data){
        var return_code = data['return_code'];
        var likes_count = data['likes_count'];
        var likes_person = data['likes_person'];

        if(return_code == 1){
            $(obj).children(".count").html(likes_count);
            $(obj).parents('div[class^="cell"]').find(".likes_person").html(likes_person);
            alert('T^T sad for this decision, but I did it for u.');
        }else{
            alert("Something goes wrong. Sorry, try again.");
            location.reload();
        }
    });
}

function answer_down(answer_id, obj){
    $.getJSON('/rango/answer_down/', {answer_id: answer_id}, function(data){
        var return_code = data['return_code'];
        var likes_count = data['likes_count'];
        var likes_person = data['likes_person'];

        if(return_code == 1){
            $(obj).prev().children(".count").html(likes_count);
            $(obj).parents('div[class^="cell"]').find(".likes_person").html(likes_person)
            alert('Thanks for your report!');
        }else{
            alert("Something goes wrong. Sorry, try again.")
            location.reload();
        }
    });
}
function answer_down_off(answer_id, obj){
    $.getJSON('/rango/answer_down_off/', {answer_id: answer_id}, function(data){
        var return_code = data['return_code'];
        var likes_count = data['likes_count'];
        var likes_person = data['likes_person'];

        if(return_code == 1){
            $(obj).prev().children(".count").html(likes_count);
            $(obj).parents('div[class^="cell"]').find(".likes_person").html(likes_person)
            alert('It\'s not an useless answer now, yeah?');
        }else{
            alert("Something goes wrong. Sorry, try again.");
            location.reload();
        }
    });
}

function button_up(obj){
    var answer_id = $(obj).attr("data-ans_id");
    if($(obj).attr("aria-pressed") == "false"){
//        if($(obj).next().attr("aria-pressed") == "true"){
//            button_down_css_off($(obj).next());
//        }
        button_down_css_off($(obj).next());

        button_up_css_on(obj);
        answer_up(answer_id, obj)
    }else{
        if(window.confirm('Are u sure to get back your love?')){
            button_up_css_off(obj);
            answer_up_off(answer_id, obj);
        }
    }
}

function button_down(obj){
    var answer_id = $(obj).prev().attr("data-ans_id");
    if($(obj).attr("aria-pressed") == "false"){
        if(window.confirm('Is this answer useless?')){
            if($(obj).prev().attr("aria-pressed") == "true"){
                button_up_css_off($(obj).prev());
            }
            button_down_css_on(obj);
            answer_down(answer_id, obj);
        }
    }else{
        button_down_css_off(obj);
        answer_down_off(answer_id, obj);
    }
}

//fancybox
$(document).ready(function() {
    $('.reply_content img').each(function() {
//        $(this).attr("alt") = "Click to see the full image.";

        var height = $(this).attr("height");
        var width = $(this).attr("width");

        if(height != null || width != null){
            if(height<width){
                if(parseInt(width) > 480){
//                    alert(1);
                    $(this).css("width", "480px");
                }
            }else{
                if(parseInt(height) > 480){
//                    alert(2);
                    $(this).css("width", "320px");
                }
            }
        }

        $(this).prop('title', 'Click to see the full image.');
        $(this).wrap("<a class=\"fancybox\" href='" + this.src + "'/>");
    });

    $(".reply_content .fancybox").fancybox({
    	openEffect	: 'elastic',
    	closeEffect	: 'elastic',
        helpers: {
          title : {
              type : 'float'
          }
        }
    });

});