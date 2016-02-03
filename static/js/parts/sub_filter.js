

function filter_init(order){
    $("#filter_btn_"+order).addClass("active");

}

function sub_filter(order){
    if(!$("#filter_btn_"+order).hasClass('active')){
        $("#filter_btn_0").removeClass("active");
        $("#filter_btn_1").removeClass("active");
        $("#filter_btn_2").removeClass("active");

        if(order[0]=='2'){
            $("#filter_btn_2").addClass("active");
        }else{
            $("#filter_btn_"+order).addClass("active");
        }

    }
}

function sub_search(url){
    var key_word = $("#sub_keyword").val();
    window.open(url+"?keyword="+key_word,"_self")
}