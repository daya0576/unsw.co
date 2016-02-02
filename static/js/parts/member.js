


function delete_member(detail_id){
    if(window.confirm('Are u sure to delete this member detail ?')){
        $.getJSON('/rango/member/delete/'+detail_id, {}, function(data){
            return_code = data['return_code']
            if(return_code == 1){
                alert('Success!')
                location.reload();
            }else{
                alert("Something goes wrong, page does not be deleted.")
            }
        });
    }
}