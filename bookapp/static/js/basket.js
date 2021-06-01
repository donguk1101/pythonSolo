$(function(){

})
$(document).ready(function(){
        mathPrice()
})
$(document).on('click','input[class^=price_input]',function(){
        let no=$(this).val()
        if(no == 0)
            no=1
        let price=$(this).parent().next().attr('price');
        tPrice=String(no*price)
        let strPrice=""
        for(i=tPrice.length; i>0;i--){
             //console.log(i)
             if(i%3==1 && i!=1){
                strPrice+=tPrice[tPrice.length-i]+","
             }else{
                strPrice+=tPrice[tPrice.length-i]
             }
        }
        $(this).parent().next().text(strPrice+'원');
        if(no <=1){
              $(this).val(1)
        }
        mathPrice()
})

function  mathPrice(){
    let tPrice=0;
    for(i=0; i<$('td[class^=price]').length;i++){
        tPrice+=Number($('td[class^=price]:eq('+i+')').text().replace(/[^0-9]/g,""));
    }
    tPrice=String(tPrice);
    let strPrice=""
        for(i=tPrice.length; i>0;i--){
             //console.log(i)
             if(i%3==1 && i!=1){
                strPrice+=tPrice[tPrice.length-i]+","
             }else{
                strPrice+=tPrice[tPrice.length-i]
             }
        }
    $('#total').text(strPrice)

}
