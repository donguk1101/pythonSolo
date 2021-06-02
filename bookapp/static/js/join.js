$(document).ready(function(){

})

$(function(){
    $('#findBtn').click(function(){
            let a=$('.zipcode_input').val()

    })

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