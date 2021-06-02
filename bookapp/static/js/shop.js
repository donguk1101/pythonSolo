$(document).on('click','.basket',function(){
        let poster=$(this).parents('.list_card').find('.poster').attr('src')
        let title=$(this).parents('.list_card').find('.title').text()
        let price=$(this).parents('.list_card').find('.price').text()
        price=price.substring(0,price.length-1)
        ordercount=1
        let id=$(this).attr('user_id');
        $.ajax({
                  type:'post',
                  data:{"poster":poster,"title":title,"price":price,"ordercount":1,"id":id},
                  url:'basketAdd',
                  success:function(result){
                        alert("장바구니에 담겼습니다.")
                  },error:function(error){
                    console.log("장바구니추가 에러")
                  }

        })
})
