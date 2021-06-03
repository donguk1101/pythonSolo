$(document).ready(function(){

})


$(document).on('click','.idBtn',function(){
   let id=$('#id_input').val()
      checkId(id)



});
$(document).on('click','#pSearchBtn',function(){
   let key=$('#pSearchInput').val();
   $('#pSearchInput').val('');
   postFind(key);

})
$(document).on('click','tr[class^=post_tr]',function(){
    let zipcode=$(this).children('.zipcode_td').text()
    let addr=$(this).children('.dong_td').text()
    $('.zipcode_input').val(zipcode)
    $('.addr_input').val(addr)

})
function postFind(key){
    $.ajax({
        type:'post',
        url:'postFind',
        data:{'key':key},
        success:function(result){
            showBungi(result)
        },error:function(error){
            console.log('우편번호 검색에러')
        }

    })
}
function showBungi(data){
    for(i=0; i<data.length;i++){
               list=data[i]
           $('#postTable').append(
                "<tr class='post_tr'>"+
                "<td class='zipcode_td'>"+list[0]+"</td>"+
                "<td class='dong_td'>"+list[1]+"</td>"+
                "</tr>"
           )


    }
}
function checkId(id){
    if(id != "" && id != undefined){
    $.ajax({
        type:'post',
        data:{'id':id},
        url:'checkId',
        success:function(result){
            if(result == 0){
                $('#id_input').val('')
                $('#id_input').attr('placeholder','id가 존재합니다')
            }else if(result == 1){
                $('#id_input').attr('placeholder','')
                alert('사용가능합니다.')
                $('#id_input').attr('readonly','true')
            }
        },error:function(error){
            console.log("중복확인 에러")
        }


    })
    }

}
