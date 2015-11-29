// likes function
$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function(data){
       $('#like_count').html(data);
       $('#likes').hide();
       $('#liked').show();
       alert('thank u for your like~');
    });
});

$('#liked').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/dislike_category/', {category_id: catid}, function(data){
       $('#like_count').html(data);
       $('#liked').hide();
       $('#likes').show();
       alert('Hoping u can like me again~')
    });
});

// search function
$('#suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/rango/suggest_category/', {suggestion: query}, function(data){
        $('#cats').html(data);
    });
});

//search navbar css
$('.search_pointer').click(function(){
    $('#nav_search').hide();
    $("#nav_search_content").show();
    $("#suggestion").focus();
});

$("#suggestion").blur(function(){
    $('#nav_search').show();
    $("#nav_search_content").hide();
});
