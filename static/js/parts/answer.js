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

function show_editor(obj, answer_id){

    $("#answer_content"+answer_id).html("<img scr='/images/favicon.ico'></img>");
    $.get('/rango/edit_description_view/', {answer_id: answer_id}, function(data){
//        $("#answer_content"+answer_id).html(data);
//        $("#answer_content"+answer_id).load("/rango/edit_description_view/?answer_id=9");
        $("#answer_content"+answer_id).html('<script id="container" name="content" type="text/plain">这里写你的初始化内容</script>')
j
    });

}

function edit_answer(obj, answer_id){
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