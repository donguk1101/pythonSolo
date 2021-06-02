$(document).ready(function(){
    let no=$('.login_row').attr('no')
    if(no==0){
            alert('아이디가 존재하지 않습니다.')
    }else if(no==-1){
            alert('비밀번호가 다릅니다.')
    }


})