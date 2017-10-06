/**
 * Created by Daya on 21/05/2016.
 */

// search function
$('#sub_keyword').keyup(function(){
    var query;
    query = $(this).val();
    var sub_name_slug = $("#sub_name_slug").val();

    $("#sub_search_loading").show();
    $('#sub_content').html("");
//    $('#nav_content').html("<i class='fa fa-refresh fa-spin fa-fw'></i>");
    $.get('/rango/sub_search/', {suggestion: query, sub_name_slug: sub_name_slug}, function(data){
        $("#sub_search_loading").hide();
        $('#sub_content').html(data);
    });
});