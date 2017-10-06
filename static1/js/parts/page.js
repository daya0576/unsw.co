
function delete_page(obj, page_id, page_name){
    if(window.confirm('Are u sure to delete page '+page_name+' ?')){
//        var page_id;
//        page_id = $(this).attr("data-pageid");
        $.getJSON('/rango/delete_cat_page/', {page_id: page_id}, function(data){
            return_code = data['return_code']
            if(return_code == 1){
                alert('Page has been deleted successfully!')
                $(obj).parent().hide();
            }else{
                alert("Something goes wrong, page didn't be deleted.")
            }
        });
    }
}