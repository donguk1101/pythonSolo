let count=0;
let time=0
let timecount=0
$(document).ready(function(){
    $('.phone').hide();
    $('.best2').hide();
    setInterval("bestSeller()", 2000)
})
function bestSeller(){
        let no=$('.best1').attr('val');
        if(no==1){
            $('.best1').attr('val','0');
            $('.best2').attr('val','1');
            $('.best1').hide()
            $('.best2').show()

        }else{
            $('.best2').attr('val','0');
            $('.best1').attr('val','1');
            $('.best2').hide()
            $('.best1').show()

        }



}
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
    $('.phone_input').attr('count','0');
    count=0;
})
function booklist_loc(tb){
    location.href="../shop?tb="+tb
}
$(document).on('keydown','.phone_input',function(key){
        if(key.keyCode==13){
                count++;
                let user_msg=$('.phone_input').val();
                makeUser_chat(user_msg);
                console.log(count)
                if(count ==1){
                    send_message();//??????
                }else if( count == 2){
                count=send_answer(count)   // count+=1
                 $('.phone_input').attr('id','second')
                }else if(count == 3){
                     thirdMessage(count)
                }else if(count == 4){
                    count=send_answer(count)

                }
                $('.phone').scrollTop($('.phone')[0].scrollHeight);
                $('.phone_input').val('')
        }
})
/*????????? ?????? ?????? ????????? ??????*/
function send_message(count){
    let msg=$('#first').val() || '';
    if(msg == "" || msg == undefined){
            count--;
        return count
        }
    $.ajax({
           type:'post',
           data:{'msg':msg},
           url:'../msg',
           success:function(result){
               let key=result['key'];
               makeFirstBot_chat(key);
           },error:function(error){
                alert("?????? ?????? ???????????????.??????????????? ?????? ??????????????????")
                count--;
           }
    })
}



function send_answer(count){
    let msg=$('#answer').val() || '';
    if(msg == "" || msg == undefined){
           count--;
        return count;
        }
    $.ajax({
           type:'post',
           data:{'msg':msg,'count':count},
           url:'../answer',
           aync:false,
           success:function(result){
                let bot_msg=result['msg']
                makeBot_chat(bot_msg);//????????? ??????
                count=result['count']
                let list=result['list']
                 $('.phone').scrollTop($('.phone')[0].scrollHeight);
                if(list.length > 0){
                    for(i=0;i<list.length; i++){
                        findNum_botChat(list[i])
                        makeBot_chat("????????? ??????????????????")
                        $('.phone').scrollTop($('.phone')[0].scrollHeight);

                    }


                }
                $('.phone_input').attr('count',Number(count)+1)
                return count
           },error:function(error){
                count--;
                makeBot_chat("?????? ?????? ???????????????. ?????? ??????????????????")

           }
    })
    console.log(count)
    return count
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

function makeFirstBot_chat(msg){
     msg=msg.trim()
    if(msg == "" || msg == undefined)
    return
    $('.phone').append(
        "<div class='bot_chat'>"+
        "<ul>"+
        "<li>"+msg+"???????????????????</li>"+
      "</ul>"+
      "<div>"
    )
    $('.phone').append(
        "<div class='bot_chat'>"+
        "<ul>"+
        "<li>??????????????? ??????????????????? </li>"+
      "</ul>"+
      "<div>"
    )
    $('.phone_input').attr('id','answer')

}
function makeBot_chat(msg){
    $('.phone').append(
        "<div class='bot_chat'>"+
        "<ul>"+
        "<li>"+msg+"</li>"+
      "</ul>"+
      "<div>"
    )
}
function thirdMessage(count){
    let msg=$('#second').val()
    if(msg == "" || msg == undefined)
    return
    makeBot_chat(msg+" ??? ????????????????")
    $('.phone_input').attr('id','answer')

}
function findNum_botChat(list){
    $('.phone').append(
        "<div class='bot_chat'>"+
        "<ul>"+
        "<li>????????????:"+list.no+"</li><br>"+
        "<li>????????????:"+list.ordertime+"</li><br>"+
      "</ul>"+
       "<ul>"+
        "<li><img src="+list.poster+"></li>"+
      "</ul>"+
      "<ul>"+
        "<li>"+list.title+"</li>"+
      "</ul>"+
      "<div>"
    )

}
