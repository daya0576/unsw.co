//delete answer
function delete_answer(answer_id){
    if(window.confirm('Are u sure to delete this answer ?')){
        $.getJSON('/rango/delete_answer/', {answer_id: answer_id}, function(data){
            return_code = data['return_code']
            if(return_code == 1){
                alert('Answer has been deleted successfully!')
                location.reload();
            }else{
                alert("Something goes wrong, page didn't be deleted.")
            }
        });
    }
}

function show_editor(answer_id){
    $(".reply_content").html("{{ answer.id }}");
}

function edit_answer(answer_id){
    $(".reply_content").html("{{ answer.id }}");

    if(window.confirm('Are u sure to delete this answer ?')){
        $.getJSON('/rango/delete_answer/', {answer_id: answer_id}, function(data){
            return_code = data['return_code']
            if(return_code == 1){
                alert('Answer has been deleted successfully!')
                location.reload();
            }else{
                alert("Something goes wrong, page didn't be deleted.")
            }
        });
    }
}