$(document).ready(function(){
    $('.phone').hide();
})

$(function(){
    $('.side_menu > li').mouseover(function(){
        $('.side_detail_menu').hide()
        let no=$(this).attr('no');
        let top=16+1.7*(no-1);
        $(this).children('.side_detail_menu').css('top',top+'em');
        $(this).children('.side_detail_menu').show()
    })
    $('.side_menu > li').mouseout(function(){
        $('.side_detail_menu').hide()
    })
})
$(document).on('click','.side_detail_menu > ul > li',function(){
    let tb=$(this).text()
    booklist_loc(tb)
})
$(document).on('click','.chat_btn',function(){
    let no=$(this).attr('value');
    if(no==0){
        $('.phone').show()
        $(this).attr('value','1')
        $(this).children().attr('class','fas fa-comment-slash fa-2x');
    }else if(no==1){
        $('.phone').hide()
        $(this).attr('value','0');
        $(this).children().attr('class','far fa-comment-dots fa-2x');
    }

})
$(document).on('click','.chat_clear',function(){
    $('.phone').children('.bot_chat').remove();
    $('.phone').children('.user_chat').remove();
    $('.phone_input').attr('id','first');
})
function booklist_loc(tb){
    location.href="../shop?tb="+tb
}
$(document).on('keydown','.phone_input',function(key){
        if(key.keyCode==13){
                let user_msg=$('.phone_input').val();
                send_message();

                makeUser_chat(user_msg);
                $('.phone').scrollTop($('.phone')[0].scrollHeight);
                $('.phone_input').val('')
        }
})
/*키워드 전송 함수 서버로 전송*/
function send_message(){
    let msg=$('#first').val();
    msg=msg.trim()
    if(msg == "" || msg == undefined)
    return
    $.ajax({
           type:'post',
           data:{'msg':msg},
           url:'../msg',
           success:function(result){
               let key=result['key'];
               makeBot_chat(key);
           },error:function(error){
                alert("메세지 전송에러")
           }
    })
}
function makeUser_chat(msg){
    msg=msg.trim()
    if(msg == "" || msg == undefined)
    return
    $('.phone').append(
        "<div class='user_chat'>"+
        "<ul>"+
        "<li>"+msg+"</li>"+
      "</ul>"+
      "<div>"
    )
}

function makeBot_chat(msg){
     msg=msg.trim()
    if(msg == "" || msg == undefined)
    return
    $('.phone').append(
        "<div class='bot_chat'>"+
        "<ul>"+
        "<li>"+msg+"하시겠습니까?</li>"+
      "</ul>"+
      "<div>"
    )
    $('.phone').append(
        "<div class='bot_chat'>"+
        "<ul>"+
        "<li>구매번호를 입력해주세요</li>"+
      "</ul>"+
      "<div>"
    )
    $('.phone_input').attr('id','second')

}

